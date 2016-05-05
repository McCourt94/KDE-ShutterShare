shuttershareApp = angular.module('shuttershareApp', ['ngMaterial','ngRoute', "ui.map", "ui.event"]);

shuttershareApp.controller('shuttershareController', function($scope,$http,$rootScope){
	console.log("loaded controller");
	
	$rootScope.images = '';
	//geolocaiton stuff...
    $scope.lat = "0";
    $scope.lng = "0";
    $scope.accuracy = "0";
    $scope.error = "";
    $scope.model = { myMap: undefined };
    $scope.myMarkers = [];
    $scope.distance = 1;
    $scope.aboutClicked = false;
    $scope.showMap = false;
    $scope.showContent = true;
    $scope.showSidebar = true;
	
	
	$scope.displayAbout = function(){
	    $scope.aboutClicked = true;
	    $scope.showContent = false;
	    $scope.showSidebar = false;
	}
	
	$scope.displayContent = function(){
        $scope.aboutClicked = false;
        $scope.showContent = true;
        $scope.showSidebar = true;
    }
	
	$scope.search = function(){
	   $scope.showMap = false;
		if(($scope.tag == "") || ($scope.tag == undefined )){
			alert("Please enter something to search");
		}else{
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/solr/',params:{"tag": $scope.tag}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $scope.returnImages = response.data;
                console.log(response.data)
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
	
	$scope.imageClick = function(image){
	    if(image.lat == "None" || image.lon == "None"){
	        alert("No location data for this image")
	        return;
	    }
	    var position = {
	        coords: {
	            longitude:image.lon,
	            latitude:image.lat
	        }
	    }
	    $scope.showMap = true;
	    $scope.showMarkerForImage(position);  
	}
	
	$scope.showMarkerForImage = function(position){
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        var latlng = new google.maps.LatLng(latitude, longitude);
        $scope.model.myMap.setCenter(latlng);
        angular.forEach($scope.myMarkers, function(marker) {
            marker.setMap(null);
        });
        $scope.myMarkers.push(new google.maps.Marker({ map: $scope.model.myMap, position: latlng }));
        google.maps.event.addListener($scope.model.myMap, 'click', function(event) {
            $scope.lat = event.latLng.lat();
            $scope.lng = event.latLng.lng();
            var pinColor = "3F51B5";
            var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor);
            var googlePosNew = new google.maps.LatLng($scope.lat,$scope.lng);
            angular.forEach($scope.myMarkers, function(marker) {
                marker.setMap(null);
            });
            var markerOpt = {
                map : $scope.model.myMap,
                position : googlePosNew,
                icon:pinImage,
                animation : google.maps.Animation.DROP
            };
            var googleMarker = new google.maps.Marker(markerOpt);
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/spatialsearch/',params:{"lat": $scope.lat,'lon':$scope.lng,'radius':$scope.distance}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $scope.returnImages = response.data
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
            });
            
        })
    }
	
    
    $scope.showResult = function () {
        return $scope.error == "";
    }
    
    $scope.mapOptions = {
        center: new google.maps.LatLng($scope.lat, $scope.lng),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
	
	$scope.getGeoLocation = function(){
       $scope.showMap = true;
	
	   if (navigator.geolocation) {
            var optn = {
                    enableHighAccuracy : true,
                    timeout : Infinity,
                    maximumAge : 0
            };
            watchId = navigator.geolocation.getCurrentPosition($scope.showPosition, $scope.showError, optn );
        } 
        else {
                alert('Geolocation is not supported in your browser');
        }
	}
	
	$scope.showPosition = function (position) {
        $scope.lat = position.coords.latitude;
        $scope.lng = position.coords.longitude;
        console.log($scope.lat,$scope.lng)
        $scope.accuracy = position.coords.accuracy;
        $scope.$apply();
        $http({
                method: 'GET',
                url: 'http://localhost:5000/python/spatialsearch/',params:{"lat": $scope.lat,'lon':$scope.lng,'radius':$scope.distance}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $scope.returnImages = response.data
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
            });
        var latlng = new google.maps.LatLng($scope.lat, $scope.lng);
        $scope.model.myMap.setCenter(latlng);
        angular.forEach($scope.myMarkers, function(marker) {
            marker.setMap(null);
        });
        $scope.myMarkers.push(new google.maps.Marker({ map: $scope.model.myMap, position: latlng }));   
        google.maps.event.addListener($scope.model.myMap, 'click', function(event) {
            $scope.lat = event.latLng.lat();
            $scope.lng = event.latLng.lng();
            var pinColor = "3F51B5";
            var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor);
            var googlePosNew = new google.maps.LatLng($scope.lat,$scope.lng);
            angular.forEach($scope.myMarkers, function(marker) {
                marker.setMap(null);
            });
            var markerOpt = {
                map : $scope.model.myMap,
                position : googlePosNew,
                icon:pinImage,
                animation : google.maps.Animation.DROP
            };
            var googleMarker = new google.maps.Marker(markerOpt);
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/spatialsearch/',params:{"lat": $scope.lat,'lon':$scope.lng,'radius':$scope.distance}
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
                $scope.returnImages = response.data
            }, function (response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                console.log(JSON.stringify(response));
                console.error("Issue retrieving data from server")
            });
            
        })
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