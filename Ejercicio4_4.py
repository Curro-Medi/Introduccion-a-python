
dic = dict()

texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor Una olla de algo mas vaca que carnero salpicon las mas noches duelos y quebrantos los sabados lantejas los viernes algun palomino de anadidura los domingos consumian las tres partes de su hacienda El resto della concluian sayo de velarte calzas de velludo para las fiestas con sus pantuflos de lo mesmo y los dias de entresemana se honraba con su velloi de lo mas fino Tenia en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte y un mozo de campo y plaza que asi ensillaba el rocin como tomaba la podadera Frisaba la edad de nuestro hidalgo con los cincuenta anos Era de complexion recia seco de carnes enjuto de rostro gran madrugador y amigo de la caza Quieren decir que tenia el sobrenombre de Quijada o Quesada que en esto hay alguna diferencia en los autores que deste caso escriben aunque por conjeturas verisimiles se deja entender que se llamaba Quijana Pero esto importa poco a nuestro cuento: basta que en la narracion del no se salga un punto de la verdad"

palabras = texto.split()


for palabra in palabras :
    dic[palabra] = dic.get(palabra,0)+1
        
print(dic)
cont = 0;

buscado = input(" Que palabra quiere que busque --> ") 

for buscar in palabras :
    if buscar == buscado :
        cont = cont + 1;

print("La palabra '", buscado, "' se muestra", cont, "veces")