function removeDuplicateFrom(array) {
  const dict = {}
  array.forEach(item => {
    if (!(item in dict))
      dict[item] = 1
    else
      dict[item] += 1
  })

  return array.filter(item => {
    return dict[item] <= 1
  })
}

module.exports = {
  removeDuplicateFrom
}
