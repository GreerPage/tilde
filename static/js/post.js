$(document).ready(function() {
    $("#first").click(function(){
        $("#id_img").click(); 
        $("#first").hide();
        $('#next-button').attr('style', 'visible');
        return false;
    });
    $('#post-botton-submit-yeah').click(function(){
        var comment = $.trim($("#caption-text-box").val());
        if(comment===''){
            $("#caption-text-box").hide()
            $('#caption-text-box').val('~caption=none~')
            var comment = $.trim($("#caption-text-box").val());
        }
        $('#id_caption').val(comment);
        $('#post-botton-submit').click();
        $('#posting-text').attr('style', 'visible');
        $('#post-botton-submit-yeah').attr('style', 'display: none;')
        return false;
    });
    $("#post-button").click(function(){
        $("#post-botton-submit").click(); 
        return false;
    });
    $('#next-button').click(function () {
        $('#image').cropper({
            aspectRatio: 16 / 16,
            //zoomable: false,
            preview: '.preview',
            crop: function(event) {
                
            }
        });
        $('#next-button').hide();
        $('#done-button').attr('style', 'visible');
    });
    $('#done-button').click(function(){
        var cropData = $('#image').cropper("getData");
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);
        $('#to-hide').hide();
        $('#done-button').hide();
        $('#preview').attr('style', 'visibility: visible');
        $('#post-botton-submit-yeah').attr('style', 'visibility: visible;');
        $('#caption-text-box').attr('style', 'visibility: visible');
    });
    $('#id_img').attr('onChange', 'img_pathUrl(this);');
});
function img_pathUrl(input){
    $('#image')[0].src = (window.URL ? URL : webkitURL).createObjectURL(input.files[0]);
    $('#image')[0].style = "";
    var fullPath = document.getElementById('id_img').value;
    if (fullPath) {
        var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        var filename = fullPath.substring(startIndex);
        if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
            filename = filename.substring(1);
        }
        if(hasWhiteSpace(filename)){
            window.location.replace(document.location.origin + "/e/500/file name cannot contain spaces");
        }
    }

}
function hasWhiteSpace(s) {
    return s.indexOf(' ') >= 0;
  }
