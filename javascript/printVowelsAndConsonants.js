function printVowelsAndConsonants(s) {
  const vowels = ['a', 'e', 'i', 'o', 'u']
  let vowelString = ''
  let consonantString = ''

  for (let i = 0; i < s.length; i++) {
    let cur = s[i]
    if (vowels.includes(cur))
      vowelString += cur
    else
      consonantString += cur
  }
  console.log(vowelString.split('').join('\n'))
  console.log(consonantString.split('').join('\n'))
}

module.exports = {
  printVowelsAndConsonants
}
