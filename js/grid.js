(function load(app){
  app.controller('AppCtrl', function($scope) {
    var IMAGES = ["https://c1.staticflickr.com/3/2481/4071767169_3467b14395_b.jpg",
    "http://www.trazeetravel.com/wp-content/uploads/2015/03/The-Crown-Liquor-Saloon-of-Belfast-Antrim-Northern-Ireland-%C2%A9-Steve-Cadman-Flickr-e1426181713163.jpg",
    "http://www.ifsa-butler.org/images/stories/sig/program-cities/qub/QUB-Background.jpg",
    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQP0uO-hjr5NDMf2H8vNHLGXDXUBmqadO49V2mHKoY1LR_EDX8w",
    "http://blog.holidaydiscountcentre.co.uk/wp-content/uploads/2013/12/belfast-via-flickr-by-iker-merodio.jpg",
    "http://www.skyscanner.net/sites/default/files/images/news/cloth_ear_belfast_urbansmoke1_flickr.jpg",
    "https://c2.staticflickr.com/4/3684/11783250866_d98e2c4792_b.jpg",
    "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTGRm8jq4_Me0fEWcu3L-YvRGrmMoWFtwQ0Fhxjhel_w0wV87px",
    "http://imgfave-herokuapp-com.global.ssl.fastly.net/image_cache/224647319.jpg",
    "http://imgfave-chat-herokuapp-com.global.ssl.fastly.net/image_cache/1340309998312341.jpg",
    "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTmhLFmlxTofs3sQcSyJ-rRkca5GxtmI19j0i-F3QDNow7ysn1y",
    "https://c1.staticflickr.com/9/8838/17304817073_44790c894a_b.jpg",
    "http://images.boomsbeat.com/data/images/full/89262/belfast_11-jpg.jpg",
    "http://www.movehub.com/sites/default/files/main_images/belfast-city-hall-550.jpg",
    "http://images6.content-wu.com/commimg/myhotcourses/blog-inline/myhc_7715.jpg",
    "http://4.bp.blogspot.com/-nuyhakv800M/TndOMD9Z98I/AAAAAAAAAH8/NAH4SGDMldQ/s1600/RISE+01.JPG",
    "http://belfastcitysightseeing.com/wp-content/uploads/2015/02/Belfast_Streets_Ahead_201109_146-copy2.jpg",
    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS6rwug5BdLw6N7bN3oyiREPERZRBc-FwQWor1vbSEGw7imiDRlSQ",
    "http://www.belfastcity.gov.uk/web/MultimediaFiles/BelfastCastleSnow1.jpg",
    "http://i.telegraph.co.uk/multimedia/archive/01209/belfast_1209991c.jpg",
    "https://anitabrowndesignstudio.files.wordpress.com/2013/09/belfast-skyline-2.jpg",
    "http://q-ec.bstatic.com/images/hotel/840x460/131/13168603.jpg",
    "http://www.travellingshopaholic.com/wp-content/uploads/2012/12/belfast-14.jpg",];
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