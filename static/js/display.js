function displayPostCaption() {
    height = $('#caption-for-posts').css('height');
    if(height === '20px') {
        $('#caption-for-posts').css('height', 'auto');
        $('#caption-button').html('less')
        $('#less').css('color', '#757575')
        $('#more-text').hide()
    }
    else {
        $('#caption-for-posts').css('height', '20px');
        $('#caption-button').html('...')
        $('#less').css('color', '#313131')
        $('#more-text').show()
    }
}