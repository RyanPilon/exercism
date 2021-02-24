//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = ([color1, color2]) => {
  return bandColors[color1] * 10 + bandColors[color2]
}

const bandColors = {
  'black' : 0,
  'brown' : 1,
  'red' : 2,
  'orange' : 3,
  'yellow' : 4,
  'green' : 5,
  'blue' : 6,
  'violet' : 7,
  'grey' : 8, 
  'white' : 9,
};
