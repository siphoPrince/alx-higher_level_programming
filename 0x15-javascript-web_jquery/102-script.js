$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
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
});

