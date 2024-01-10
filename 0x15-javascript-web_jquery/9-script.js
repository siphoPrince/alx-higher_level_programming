$(document).ready(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.error('Error fetching translation:', textStatus, errorThrown);
    }
  });
});

