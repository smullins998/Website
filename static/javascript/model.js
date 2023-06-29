function handlePicklistChange() {
  var picklist = document.getElementById('myPicklist');
  var image = document.getElementById('myImage');
  var selectedOption = picklist.value;

  if (selectedOption === 'RF') {
    image.src = 'static/RF.png';
  } else if (selectedOption === 'SVM') {
    image.src = 'static/SVM.png';
  } else if (selectedOption === 'KNN') {
    image.src = 'static/KNN.png';
  } else if (selectedOption === 'MLP') {
    image.src = 'static/MLP.png';
  } else {
    // Default image source if no option is selected or option doesn't match any condition
    image.src = 'MLP.png';
  }
}
