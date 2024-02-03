
    $(document).ready(function () {
   /*      const toggleAddFormButton = $('#toggleAddForm');
        const addFormContainer = $('#addFormContainer');
        const addDestinationForm = $('#addDestinationForm');

        toggleAddFormButton.click(function () {
            // Toggle the visibility of the form
            addFormContainer.toggle();
        });

        addDestinationForm.submit(function (event) {
            event.preventDefault();

            // Handle form submission (e.g., send data to the server)

            // Clear form fields
            addDestinationForm[0].reset();

            // Hide the form after submission
            addFormContainer.hide();
        }); */
        
    });
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
    });