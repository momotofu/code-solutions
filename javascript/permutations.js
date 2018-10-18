function convertToLetters(number) {
  let s = ''
  const numberString = String(number)
  for (let i = 0; i < numberString.length; i++) {
    s += String.fromCharCode(96 + Number(numberString[i]))
  }

  return s
}

module.exports = {
  convertToLetters
}
