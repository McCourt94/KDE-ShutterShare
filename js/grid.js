(function load(app){
  app.controller('AppCtrl', function($scope) {
    var IMAGES = ['https://farm1.staticflickr.com/750/23456707155_095a9f16cf_b.jpg',
'https://farm8.staticflickr.com/7488/15664490410_3dc1a99796_b.jpg',
'https://farm6.staticflickr.com/5567/14749709315_4b30a18a5f_b.jpg',
'https://farm4.staticflickr.com/3925/14563032070_e2fb67bd79_b.jpg',
'https://farm3.staticflickr.com/2912/14749708575_65f8c35532_b.jpg',
'https://farm4.staticflickr.com/3898/14726710856_11e86c82b2_b.jpg',
'https://farm4.staticflickr.com/3871/14747364964_8df5eefb58_b.jpg',
'https://farm6.staticflickr.com/5555/14747364744_5799e6b365_b.jpg',
'https://farm4.staticflickr.com/3730/14106308527_5177b32e69_b.jpg',
'https://farm4.staticflickr.com/3799/13893149584_384c7c74e2_b.jpg',
'https://farm4.staticflickr.com/3737/9076283592_eba7f8326e_b.jpg',
'https://farm4.staticflickr.com/3820/9076283470_a117748b3f_b.jpg',
'https://farm6.staticflickr.com/5492/9074053337_433d4c35e3_b.jpg',
'https://farm3.staticflickr.com/2863/9074053289_be1423673d_b.jpg',
'https://farm8.staticflickr.com/7372/9076283192_432b3e82b5_b.jpg',
'https://farm4.staticflickr.com/3710/9074053187_7e96ebe61c_b.jpg',
'https://farm3.staticflickr.com/2821/9074053005_b3c5a46031_b.jpg',
'https://farm8.staticflickr.com/7381/9076283092_e3646df615_b.jpg',
'https://farm8.staticflickr.com/7370/9076282934_f3fb618abb_b.jpg',
'https://farm8.staticflickr.com/7333/9076282800_08ddd7002e_b.jpg',
'https://farm6.staticflickr.com/5537/9076282690_fe480178cb_b.jpg',
'https://farm8.staticflickr.com/7418/9076282680_7c851f3567_b.jpg',
'https://farm4.staticflickr.com/3770/9076282608_f5b7eb32b9_b.jpg',
'https://farm3.staticflickr.com/2825/9074052465_e43cbaed1e_b.jpg',
'https://farm8.staticflickr.com/7295/9074052451_6f5c4a78cf_b.jpg',
'https://farm6.staticflickr.com/5521/9074052355_c06dcabf7f_b.jpg',
'https://farm4.staticflickr.com/3783/9076282390_a46f9c7c8e_b.jpg',
'https://farm4.staticflickr.com/3690/9076282260_ea51a3f1a0_b.jpg',
'https://farm4.staticflickr.com/3764/9074052191_83fbcf3103_b.jpg',
'https://farm8.staticflickr.com/7408/9074052163_e528f340be_b.jpg',
'https://farm4.staticflickr.com/3730/9074052127_d4512a3c61_b.jpg',
'https://farm6.staticflickr.com/5461/9076282070_64e1773aa8_b.jpg',
'https://farm4.staticflickr.com/3777/9074051979_cf9f77eaa5_b.jpg',
'https://farm8.staticflickr.com/7404/9076282040_539a38f896_b.jpg',
'https://farm8.staticflickr.com/7286/9076281996_2555272d2d_b.jpg',
'https://farm4.staticflickr.com/3726/9076281914_8c367fd0fc_b.jpg',
'https://farm3.staticflickr.com/2818/9076281926_9676b47cf4_b.jpg',
'https://farm8.staticflickr.com/7303/9074051749_97205dff79_b.jpg',
'https://farm8.staticflickr.com/7381/9076281756_6eb845e82d_b.jpg',
'https://farm3.staticflickr.com/2876/9076281764_b45c3d589a_b.jpg',
'https://farm6.staticflickr.com/5538/9076281574_b68a49926a_b.jpg',
'https://farm8.staticflickr.com/7403/9076281554_9b3d9bbb38_b.jpg',
'https://farm6.staticflickr.com/5457/8846998860_ae937a316c_b.jpg',
'https://farm3.staticflickr.com/2861/8817184798_e4d7dc6218_b.jpg',
'https://farm9.staticflickr.com/8529/8574750784_b41ff9631b_b.jpg',
'https://farm9.staticflickr.com/8215/8300153645_75e5f65bfb_b.jpg',
'https://farm9.staticflickr.com/8195/8128213673_324f4a395d_b.jpg',
'https://farm9.staticflickr.com/8045/8108803499_c8c59a10a0_b.jpg',
'https://farm9.staticflickr.com/8294/7745774098_1db8d9ffd2_b.jpg',
'https://farm6.staticflickr.com/5083/5294113739_44e4eedcf4_b.jpg',
'https://farm5.staticflickr.com/4148/5223100763_f8c68cbd11_b.jpg',
'https://farm5.staticflickr.com/4083/5223697810_1e47f8a3fd_b.jpg',
'https://farm6.staticflickr.com/5130/5223100575_f98dd6d775_b.jpg',
'https://farm8.staticflickr.com/7325/13892807213_f49fa6440c_b.jpg',
'https://farm6.staticflickr.com/5245/5223100465_17b8f89b50_b.jpg'];
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