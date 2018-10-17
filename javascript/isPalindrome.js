function isPalindrome(s) {
  const baseString = s.split(' ').join('').toLowerCase()
  const reverseString = baseString.split('').reverse().join('')
  return baseString === reverseString;
}

module.exports = {
  isPalindrome
}
