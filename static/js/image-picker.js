// set image properties, for Highlight effect added when click
var imgProp = {
  'padding': '3px',
  'backgroundColor': '#000000',
  'borderSize': '2ps',
  'borderStyle': 'dashed',
  'borderColor': '#0001fe'
 };
 
 // function to highlight IMGs on click - from: https://coursesweb.net/
 function highlightImg() {
  // gets all <img> tags, and their number
  var allimgs = document.getElementsByTagName('img');
  var nrallimgs = allimgs.length;
 
  // traverses the <img> elements, and register onclick to each one
  // else, apply the properties defined in $imgProp
  for(i=0; i<nrallimgs; i++) {
  allimgs[i].onclick=function() {
  // if borderStyle is already applied, anulates the 'padding', 'background' and 'border' properties
  if(this.style.borderStyle == imgProp.borderStyle) {
  this.style.padding = 'auto';
  this.style.background = 'none';
  this.style.border = 'none';
  }
  else {
  this.style.padding = imgProp.padding;
  this.style.backgroundColor = imgProp.backgroundColor;
  this.style.borderSize = imgProp.borderSize;
  this.style.borderStyle = imgProp.borderStyle;
  this.style.borderColor = imgProp.borderColor;
  }
  }
  }
 }
 
 // calls the highlightImg() function to apply the effect
 highlightImg();