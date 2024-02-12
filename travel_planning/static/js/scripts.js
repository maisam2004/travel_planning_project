
    $(document).ready(function () {

        var originalText = $('#addDestinationText').text();

        // Change the text on hover
        $('.btn-primary').hover(
            function () {
                $('#addDestinationText').text('Login first');
            },
            function () {
                // Restore the original text when not hovering
                $('#addDestinationText').text(originalText);
            }
        );

        
   
    $('.like-button').click(function() {
        var icon = $(this);
        if (icon.hasClass('liked')) {
            icon.removeClass('liked').addClass('notliked'); // change class for unlike
        } else {
            icon.removeClass('notliked').addClass('liked'); // change class for like
        }
    });

    });