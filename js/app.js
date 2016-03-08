shuttershareApp = angular.module('shuttershareApp', ['ngMaterial','ngRoute']);

shuttershareApp.controller('shuttershareController', function($scope,$http){
	console.log("loaded controller");
	$scope.search = function(){


		if(($scope.tag == "") || ($scope.tag == undefined )){
			console.log("Please enter something to search");
		}else{
            $http({
                method: 'GET',
                url: 'http://localhost:5000/python/solr/'+$scope.tag
            }).then(function (response) {
                // this callback will be called asynchronously
                // when the response is available
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
});