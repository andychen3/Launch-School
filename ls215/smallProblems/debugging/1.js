// https://launchschool.com/exercises/eb705274



let ladder = ''

['head', 'heal', 'teal', 'tell', 'tall', 'tail'].forEach(word => {
  if (ladder !== '') {
    ladder += '-'
  }

  ladder += word
})

console.log(ladder)  // expect: head-heal-teal-tell-tall-tail

// Because of no semicolons. The automatic semicolon insertion combines line
// 5 and 7.