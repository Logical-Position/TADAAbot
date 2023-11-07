document.addEventListener('DOMContentLoaded', attachComponents);

// MARK: Radio-Radio Component

function handleRadioRadioChange(q, toEnable) {
    // Secondary options become available once yes is checked, might be a cleaner way to do this later.
    const secondaryInputs = document.querySelectorAll(`input[name^=${q}][data-rrs=""]`);
    console.log(secondaryInputs);
    if (toEnable) {
        enableSecondaryRadioInputs(secondaryInputs);
    } else {
        disableSecondaryRadioInputs(secondaryInputs);
    }
}

function enableSecondaryRadioInputs(secondaryInputs) {
    console.log(secondaryInputs);
    secondaryInputs.forEach(item => item.disabled = false);
}

function disableSecondaryRadioInputs(secondaryInputs) {
    secondaryInputs.forEach(item => item.disabled = true);
}

// MARK: Dynamic Text "Component"
//class DynamicTextComponent() {}

function updateInputValue(input, value) {
    console.log(input);
    console.log(value);
    input.value = value;
    console.log(input.value);
}

function updateTextArea(input, textarea, formInput) {
    textarea.innerText = input.value;
    updateInputValue(formInput, input.value);
}

function attachComponents() {
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

        // MARK: Radio-Radio Components
        // const rrComponents = document.querySelectorAll(".things-n-stuff");
        // rrComponents.forEach((comp) => {
        //     const id = comp.querySelector('input').name;
        //     const inputs = comp.querySelectorAll(`input[name='${id}']`);
        //     inputs.forEach((input) => {
        //         input.addEventListener("change", function(e) {
        //             const q = input.getAttribute('name');
        //             const toEnable = input.value === 'yes';
        //             handleRadioRadioChange(q, toEnable);
        //         });
        //     })
        // });

        // MARK: Dynamic Text Component
        const dtComps = document.querySelectorAll('[data-comp="dynamic-text"]');
        dtComps.forEach((comp) => {
            // const inputs = comp.querySelectorAll(`input[type="radio"]`);
            const dropdown = comp.querySelector(`select`);
            const textarea = comp.querySelector(`div[contenteditable="true"]`);
            const formInput = comp.querySelector(`input[type="text"]`);
            dropdown.addEventListener("change", function(e) {
                updateTextArea(dropdown, textarea, formInput);
            });
            textarea.addEventListener("input", function(e) {
                updateInputValue(formInput, textarea.innerText);
            });
            // inputs.forEach((input, index) => {
            //     if (index === 0) {
            //         input.checked = true;
            //         updateTextArea(input, textarea, formInput);
            //     }

            //     input.addEventListener("change", function(e) {
            //         if (input.checked) {
            //             updateTextArea(input, textarea, formInput);
            //         }
            //     });
            // });
        });
    } catch (e) {
        console.error(e);
    }
}