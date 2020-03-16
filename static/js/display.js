function displayPostCaption() {
    height = $('#caption-for-posts').css('height');
    if(height === '40px') {
        $('#caption-for-posts').css('height', 'auto');
        $('#caption-button').html('show less')
        $('#less').css('color', '#757575')
        $('#more-text').hide()
    }
    else {
        $('#caption-for-posts').css('height', '40px');
        $('#caption-button').html('show more')
        $('#less').css('color', '#313131')
        $('#more-text').show()
    }
}