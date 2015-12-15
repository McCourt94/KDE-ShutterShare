$(function() {
    $( "#location-slider" ).slider({
        range: "min",
        value: 0,
        min: 1,
        max: 15,
    });
      $( "#location-slider" ).css('background', '#384cbd');
      $( "#location-slider .ui-slider-range" ).css('background', '#dae5ff');
  });

$(function() {
    $( "#time-slider" ).slider({
        range: "min",
        value: 0,
        min: 1,
        max: 10,
    });
      $( "#time-slider" ).css('background', '#384cbd');
      $( "#time-slider .ui-slider-range" ).css('background', '#dae5ff');
  });

