function factorial(n) {
  if (n === 1)
    return n
  return factorial(n - 1) * n
}

module.exports = {
  factorial
}
