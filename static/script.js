const add_symptom_btn = document.querySelector('.add-symptom');
let symptoms_entered = document.querySelector('.symptoms-entered');
const symptom_form = document.querySelector('.symptom-form');
// when add symptom button is pressed, do the following
add_symptom_btn.addEventListener("click", function(e) {
    e.preventDefault()
    let symptom = document.querySelector('.symptom').value;
    // if symptom field is not empty, add this to the list
    // of symptoms selected by the user.
    // make a button for this, which when clicked  will
    // disappear from the list
    if (symptom != "") {
      let b = document.createElement('BUTTON');
      let text = document.createTextNode('X ' + symptom);
      b.className = 'added-symptom';
      b.appendChild(text);
      // remove the element when it gets clicked
      b.addEventListener("click", function() {
        this.parentNode.removeChild(this);
      })
      symptoms_entered.appendChild(b);
      document.querySelector('.symptom').value = "";

    }
});
