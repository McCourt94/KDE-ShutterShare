shuttershareApp = angular.module('shuttershareApp', ['ngMaterial','ngRoute', "ui.map", "ui.event"]);

shuttershareApp.controller('shuttershareController', function($scope,$http,$rootScope){
	console.log("loaded controller");
	console.log($scope.location);
	
	$rootScope.images = '';
	
	
	
	$scope.search = function(){
		if(($scope.tag == "") || ($scope.tag == undefined )){
			console.log("Please enter something to search");
		}else{
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/solr/',params:{"tag": $scope.tag}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $rootScope.images = response.data
                console.log(response.data);
                $scope.tag=''
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
            });
            console.log($scope.tag);
		}
	}
	
	
	
	
	//geolocaiton stuff...
	$scope.lat = "0";
    $scope.lng = "0";
    $scope.accuracy = "0";
    $scope.error = "";
    $scope.model = { myMap: undefined };
    $scope.myMarkers = [];
    $scope.distance = 1;
    $scope.showMap = false;
    
    $scope.showResult = function () {
        return $scope.error == "";
    }
    
    $scope.mapOptions = {
        center: new google.maps.LatLng($scope.lat, $scope.lng),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
	
	$scope.geoLoc = function(){
	
       $scope.showMap = true;
	
	   if (navigator.geolocation) {
            var optn = {
                    enableHighAccuracy : true,
                    timeout : Infinity,
                    maximumAge : 0
            };
            watchId = navigator.geolocation.watchPosition($scope.showPosition, $scope.showError, optn);
            

        } 
        else {
                alert('Geolocation is not supported in your browser');
        }
	}
	
	$scope.showPosition = function (position) {
        $scope.lat = position.coords.latitude;
        $scope.lng = position.coords.longitude;
        $scope.accuracy = position.coords.accuracy;
        console.log($scope.distance)
        $scope.$apply();
        $http({
                method: 'GET',
                url: 'http://localhost:5000/python/geo_search/',params:{"lat": $scope.lat,'lon':$scope.lng,'radius':$scope.distance}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $rootScope.images = response.data
                console.log(response.data);
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
        });
        var latlng = new google.maps.LatLng($scope.lat, $scope.lng);
        $scope.model.myMap.setCenter(latlng);
        $scope.myMarkers.push(new google.maps.Marker({ map: $scope.model.myMap, position: latlng }));
        google.maps.event.addListener($scope.model.myMap, 'click', function(event) {
            $scope.lat = event.latLng.lat();
            $scope.lng = event.latLng.lng();
            var pinColor = "3F51B5";
            var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor);
            var googlePosNew = new google.maps.LatLng($scope.lat,$scope.lng);
            var markerOpt = {
                map : $scope.model.myMap,
                position : googlePosNew,
                icon:pinImage,
                animation : google.maps.Animation.DROP
            };
            var googleMarker = new google.maps.Marker(markerOpt);
            // populate yor box/field with lat, lng
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/geo_update/',params:{"lat": $scope.lat,'lon':$scope.lng}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $rootScope.images = response.data
                console.log(response.data);
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
            });
            console.log($scope.lat,$scope.lng);
            
        });
    }
    
    $scope.showError = function (error) {
        switch (error.code) {
            case error.PERMISSION_DENIED:
                $scope.error = "User denied the request for Geolocation."
                break;
            case error.POSITION_UNAVAILABLE:
                $scope.error = "Location information is unavailable."
                break;
            case error.TIMEOUT:
                $scope.error = "The request to get user location timed out."
                break;
            case error.UNKNOWN_ERROR:
                $scope.error = "An unknown error occurred."
                break;
        }
        $scope.$apply();
    }
});