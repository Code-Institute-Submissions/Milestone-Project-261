$(document).on('click', function() {
    $('.collapse').collapse('hide');
});

$('.edit-comment').each(function() {

    var comment_text = 'comment-text-' + $(this).attr('id');
    var edit_comment = 'edit-crypto-comment-' + $(this).attr('id');
    var delete_comment = 'delete-comment-' + $(this).attr('id');

    $(this).click(function() {
        /* https://www.w3schools.com/jquery/css_css.asp */
        /* When the edit button is clicked the edit form will appear and the orginal comment, edit and delete button will disappear */
        $('#' + comment_text).css('display', 'none');
        $('#' + edit_comment).css('display', 'block');
        $('.edit-comment').css('display', 'none');
        $('#' + delete_comment).css('display', 'none');
    });

});

/* When the cancel button is clicked the edit form will disappear and the orginal comment will reappear */
$('.cancel-edit-comment').on('click', function() {
    $('.comment-text').css('display', 'block');
    $('.edit-crypto-comment').css('display', 'none');
    $('.edit-comment').css('display', 'block');
    $('.delete-comment').css('display', 'block');

});