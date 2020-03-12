$(document).ready(function() {
    $("#first").click(function(){
        $("#id_img").click(); 
        return false;
    });
    $("#post-button").click(function(){
        $("#post-botton-submit").click(); 
        return false;
    });
    $('#image').on('load', function () {
        $('#image').cropper({
            aspectRatio: 16 / 16,
            zoomable: false,
            preview: '.preview',
            crop: function(event) {
                
            }
        });
    });
    $('#done-button').click(function(){
        var cropData = $('#image').cropper("getData");
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);
        $('#to-hide').hide()
    });
    $('#post-button').click(function(){
        var cropData = $image.cropper("getData");
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);
        $("#post-button").submit();
    });
    $('#id_img').attr('onChange', 'img_pathUrl(this);')
    $('#imgformW').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
});
function img_pathUrl(input){
    $('#image')[0].src = (window.URL ? URL : webkitURL).createObjectURL(input.files[0]);
    $('#image')[0].style = "";
}
