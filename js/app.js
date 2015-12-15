shuttershareApp = angular.module('shuttershareApp', ['ngMaterial','ngRoute']);

shuttershareApp.controller('shuttershareController', function($scope){
	console.log("loaded controller");
	$scope.search = function(){


		if(($scope.city == "" && $scope.tag == "") || ($scope.city == undefined && $scope.tag == undefined )){
			console.log("Please enter something to search");
		}else{
			console.log("You are searching for: " + $scope.tag + " in " + $scope.city);
			$scope.city = "";
			$scope.tag = "";
		}


	}
});