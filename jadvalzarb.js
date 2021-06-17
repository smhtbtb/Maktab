const number = parseInt(prompt('Enter an integer: '));
document.write("<center><table style='text-align: center;' border='1px solid red'>");
// let row = ''
for(let i = 1; i <= number; i++) {
    document.write("<tr>")
    for(let j = 1; j <= number; j++) {
        document.write("<td style='padding: 5px'>" + i * j + "</td>");
        // row += (i*j + '\t');
    }
    document.write("</tr>");
    // console.log(row + '\n')
    // row = ''
}
document.write("</center></table>");
