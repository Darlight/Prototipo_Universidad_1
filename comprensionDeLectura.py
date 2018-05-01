preguntas_articulo_Tabaco_frena_el_desarrollo_en_Guatemala={"Pregunta1": ["1)Respuesta","2)Respuesta "],"Pregunta2":["1)Respuesta","2)Respuesta"]}
preguntas_articulo_Impulsan_mejores_contorles={"Pregunta1": ["1)Respuesta","2)Respuesta "],"Pregunta2":["1)Respuesta","2)Respuesta"]}
correctas=0
incorrectas=0
total_correctas=0
total_incorrectas=0
questionario= input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n")
while(questionario !="3"):
   if(questionario=="1"):
      preguntas=preguntas_articulo_Tabaco_frena_el_desarrollo_en_Guatemala.keys()
      for pregunta in preguntas:
         print(pregunta)
         opciones=preguntas_articulo_Tabaco_frena_el_desarrollo_en_Guatemala[pregunta]
         for a in opciones:
            print(a)
         print("")
      respuesta1=input("Ingrese la respuesta de la pregunta 1\n")
      respuesta2=input("Ingrese la respuesta de la pregunta 2\n")
      if(respuesta1=="2"):
          correctas+=1
          total_correctas+=1
      else:
          incorrectas+=1
          total_incorrectas+=1
      if(respuesta2=="2"):
          correctas+=1
          total_correctas+=1
      else:
          incorrectas+=1
          total_incorrectas+=1
      print("Respuestas correctas: "+str(correctas))
      print("Respuestas incorrectas: "+str(incorrectas))
      correctas=0
      incorrectas=0
      questionario= input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n")
   if(questionario=="2"):
      preguntas=preguntas_articulo_Impulsan_mejores_contorles.keys()
      for pregunta in preguntas:
         print(pregunta)
         opciones=preguntas_articulo_Tabaco_frena_el_desarrollo_en_Guatemala[pregunta]
         for a in opciones:
            print(a)
         print("")
      respuesta1=input("Ingrese la respuesta de la pregunta 1\n")
      respuesta2=input("Ingrese la respuesta de la pregunta 2\n")
      if(respuesta1=="1"):
          correctas+=1
          total_correctas+=1
      else:
          incorrectas+=1
          total_incorrectas+=1
      if(respuesta2=="2"):
          correctas+=1
          total_correctas+=1
      else:
          incorrectas+=1
          total_incorrectas+=1
      print("Respuestas correctas: "+str(correctas))
      print("Respuestas incorrectas: "+str(incorrectas))
      correctas=0
      incorrectas=0
      questionario= input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n")
   if(questionario==3):
      questionario=3
   else:
      print("Esa no es una opcion del menu")
      questionario= input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n")
print("Total de respuestas correctas: "+str(total_correctas))
print("Total de respuestas incorrectas: "+str(total_incorrectas))
