(function load(app){
  app.controller('AppCtrl', function($scope) {
    var IMAGES = [
    ];
    $scope.tiles = []
    for (var i = 0; i < 100; i++) {
    $scope.tiles.push({
        src: randomImage(),
        colspan: randomSpan(),
        rowspan: randomSpan()
      })
    }
    function randomImage(){
      return IMAGES[Math.floor(Math.random() * IMAGES.length)];
    }  
    function randomSpan() {
      var r = Math.random();
      if (r < 0.8) {
        return 1;
      } else if (r < 0.9) {
        return 2;
      } else {
        return 3;
      }
    }
  });})(shuttershareApp);