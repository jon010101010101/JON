#!/usr/bin/env python3
# coding: utf-8

# Importamos el módulo traceback y las clases Elem y Text del archivo elem.py
import traceback
from elem import Elem, Text

# Definimos una función para probar la funcionalidad de la clase Text
def test_text():
    """
    Prueba la funcionalidad de la clase Text.
    """
    # Verificamos si Text es una instancia de str
    assert isinstance(Text(), str)  # Comprobación básica de tipo
    # Comportamiento por defecto: Text sin argumentos debe ser vacío
    assert str(Text()) == ''  # Verificación del comportamiento por defecto
    # Comportamiento con un argumento vacío
    assert str(Text('')) == ''  # Verificación con argumento vacío
    # Comportamiento con un argumento no vacío
    assert str(Text('foo')) == 'foo'  # Verificación con un argumento no vacío
    # Reemplazo de patrones: salto de línea se convierte en <br />
    assert str(Text('\n')) == '\n<br />\n'  # Reemplazo de salto de línea
    # Reemplazo de patrones: múltiples saltos de línea
    assert str(Text('foo\nbar')) == 'foo\n<br />\nbar'  # Reemplazo de múltiples saltos
    # Escapando caracteres especiales: <
    assert str(Text('<')) == '&lt;'  # Escapar <
    # Escapando caracteres especiales: >
    assert str(Text('>')) == '&gt;'  # Escapar >
    # Escapando caracteres especiales: "
    assert str(Text('"')) == '&quot;'  # Escapar "
    print('Text behaviour : OK.')  # Mensaje de éxito

# Definimos una función para probar la funcionalidad básica de la clase Elem
def test_elem_basics():
    """
    Prueba la funcionalidad básica de la clase Elem.
    """
    # Comportamiento por defecto: Elem sin argumentos debe ser un div vacío
    assert str(Elem()) == '<div></div>'  # Verificación del comportamiento por defecto
    # Orden de los argumentos: tag, attr, content, tag_type
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'  # Verificación del orden de argumentos
    # Nombres de los argumentos: tag, attr, content, tag_type
    assert str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')) == '<body>\n  <div></div>\n</body>'  # Verificación de nombres de argumentos
    # Con elem como contenido: anidamiento de elementos
    assert str(Elem(content=Elem())) == '<div>\n  <div></div>\n</div>'  # Verificación del anidamiento
    # Con lista como contenido: múltiples elementos
    assert str(Elem(content=[Text('foo'), Text('bar'), Elem()])) == '<div>\n  foo\n  bar\n \
 <div></div>\n</div>'  # Verificación con lista de contenido
    print('Basic Elem behaviour : OK.')  # Mensaje de éxito

# Definimos una función para probar el manejo de textos vacíos en Elem
def test_empty_texts():
    """
    Prueba el manejo de textos vacíos en Elem.
    """
    # Verificación de texto vacío como contenido
    assert str(Elem(content=Text(''))) == '<div></div>'  # Verificación de texto vacío
    # Verificación de lista de textos vacíos como contenido
    assert str(Elem(content=[Text(''), Text('')])) == '<div></div>'  # Verificación de lista vacía
    # Verificación de mezcla de textos vacíos y no vacíos
    assert str(Elem(content=[Text('foo'), Text(''), Elem()])) == '<div>\n  foo\
\n  <div></div>\n</div>'  # Verificación de mezcla de textos
    print('Elem with empty texts : OK.')  # Mensaje de éxito

# Definimos una función para probar el manejo de errores en la clase Elem
def test_errors():
    """
    Prueba el manejo de errores en la clase Elem.
    """
    # Error de tipo si el contenido no es Text o Elem
    try:
        # Intentamos crear un Elem con contenido no válido (entero)
        Elem(content=1)
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert type(e) == Elem.ValidationError  # Comprobación de tipo de excepción
    # La forma correcta: contenido debe ser Text o Elem
    assert str(Elem(content=Text(1))) == '<div>\n  1\n</div>'  # Verificación de contenido válido

    # Error de tipo si los elementos de la lista no son instancias de Text o Elem
    try:
        # Intentamos crear un Elem con lista de contenido no válido
        Elem(content=['foo', Elem(), 1])
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert type(e) == Elem.ValidationError  # Comprobación de tipo de excepción
    # La forma correcta: todos los elementos deben ser Text o Elem
    assert (str(Elem(content=[Text('foo'), Elem(), Text(1)]))
            == '<div>\n  foo\n  <div></div>\n  1\n</div>')  # Verificación de lista válida

    # Lo mismo con add_method()
    try:
        # Creamos un Elem vacío
        elem = Elem()
        # Intentamos añadir contenido no válido (entero)
        elem.add_content(1)
        # Si no se lanza excepción, es un comportamiento incorrecto
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert isinstance(e, Elem.ValidationError)  # Comprobación de tipo de excepción
    
    # O con listas:
    try :
        # Creamos un Elem vacío
        elem = Elem()
        # Intentamos añadir lista con contenido no válido
        elem.add_content([1,])
        # Si no se lanza excepción, es un comportamiento incorrecto
        raise(Exception('incorrect behaviour'))
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert isinstance(e, Elem.ValidationError)  # Comprobación de tipo de excepción

    # str no se puede usar:
    try:
        # Creamos un Elem vacío
        elem = Elem()
        # Intentamos añadir lista con texto vacío
        elem.add_content(['',])
        # Si no se lanza excepción, es un comportamiento incorrecto
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert isinstance(e, Elem.ValidationError)  # Comprobación de tipo de excepción
    
    try:
        # Intentamos crear un Elem con contenido vacío (cadena vacía)
        elem = Elem(content='')
        # Si no se lanza excepción, es un comportamiento incorrecto
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verificamos que se lanza la excepción correcta
        assert isinstance(e, Elem.ValidationError)  # Comprobación de tipo de excepción
    print('Error cases : OK.')  # Mensaje de éxito

# Definimos una función para probar el anidamiento de elementos Elem
def test_embedding():
    """
    Prueba el anidamiento de elementos Elem.
    """
    # Verificación del anidamiento de múltiples niveles
    assert (str(Elem(content=Elem(content=Elem(content=Elem()))))
            == """<div>
  <div>
    <div>
      <div></div>
    </div>
  </div>
</div>""")
    print('Element embedding : OK.')  # Mensaje de éxito

# Definimos una función para ejecutar todas las pruebas
def test():
    """
    Ejecuta todas las pruebas.
    """
    # Llamamos a cada función de prueba
    test_text()
    test_elem_basics()
    test_embedding()
    test_empty_texts()
    test_errors()conda 
    
if __name__ == '__main__':
    try :
        # Ejecutamos la función de prueba principal
        test()
        print('Tests succeeded!')  # Mensaje de éxito
    except AssertionError as e:
        # Si ocurre un error, imprimimos el traceback y el mensaje de error
        traceback.print_exc()
        print(e)
        print('Tests failed!')  # Mensaje de fallo


"""
"Text behaviour : OK."

Indica que la clase Text funciona correctamente, incluyendo el manejo de 
caracteres especiales y saltos de línea.

"Basic Elem behaviour : OK."

Confirma que la funcionalidad básica de la clase Elem es correcta, incluyendo la 
creación de elementos simples y compuestos.

"Element embedding : OK."

Verifica que los elementos se pueden anidar correctamente, lo cual es crucial 
para estructuras HTML complejas.

"Elem with empty texts : OK."

Demuestra que tu implementación maneja correctamente los textos vacíos, un caso 
importante en HTML.

"Error cases : OK."

Confirma que tu clase maneja adecuadamente los casos de error, lanzando las 
excepciones apropiadas cuando se intenta añadir contenido inválido.

"Tests succeeded!"

Esta es la confirmación final de que todas las pruebas pasaron sin errores.

"""