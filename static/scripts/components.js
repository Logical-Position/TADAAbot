document.addEventListener('DOMContentLoaded', addComponents);

function addComponents() {
    try {
        // MARK: Hidden Input Component
        let hiddenInputs = document.querySelectorAll('.hidden-input');
        for (let inputElement of hiddenInputs) {
            let parentSelect = inputElement.previousElementSibling;
            parentSelect.addEventListener('change', function() {
                if (parentSelect.value === 'other') {
                    inputElement.classList.remove('hidden-input');
                } else {
                    inputElement.classList.add('hidden-input');
                }
            });
        }

        // MARK: Dynamic Text Component
        const dtComps = document.querySelectorAll('[data-comp="dynamic-text"]');
        dtComps.forEach((comp) => {
            const inputs = comp.querySelectorAll(`input[type="radio"]`);
            const textarea = comp.querySelector(`div[contenteditable="true"]`);
            const formInput = comp.querySelector(`input[type="text"]`);
            inputs.forEach((input, index) => {
                if (index === 0) {
                    input.checked = true;
                    handleDynamicTextChange(input, textarea, formInput);
                }

                input.addEventListener("change", function(e) {
                    if (input.checked) {
                        handleDynamicTextChange(input, textarea, formInput);
                    }
                });
            })
        });
    } catch (e) {
        console.error(e);
    }
}