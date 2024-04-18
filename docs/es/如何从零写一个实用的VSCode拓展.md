# Cómo escribir una extensión útil de VS Code desde cero (en proceso)

VS Code es un editor muy útil que cuenta con un poderoso ecosistema de extensiones, lo que permite a los usuarios instalar o publicar libremente extensiones para mejorar las funcionalidades del software.

Este artículo proviene de una necesidad personal, que gira en torno al desarrollo de una herramienta de panel útil, detallando cómo escribir desde cero y publicar tu propia extensión de VS Code.

## Identificar la necesidad

Cuando tienes una necesidad, lo primero que debes hacer es buscar en la tienda de extensiones de VS Code aquellas que se ajusten a tus necesidades, en lugar de reinventar la rueda. Solo deberías considerar desarrollar una extensión propia si encuentras que las aplicaciones desarrolladas por otros no cumplen con tus requerimientos, o si carecen de las funciones que deseas.

En el ejemplo de este artículo, quería una herramienta de panel que pudiera convertir mis documentos Markdown en una vista de panel concisa con un solo clic, para poder ver todas las tareas actuales de un vistazo. Sin embargo, las extensiones relacionadas con paneles disponibles no estaban basadas en archivos Markdown, no permitían la actualización en tiempo real de la vista de panel, e incluso no eran lo suficientemente concisas. En resumen, ninguna extensión cumplía con mis necesidades. Por lo tanto, decidí crear una por mi cuenta.

## Establecer el marco de trabajo

El primer paso para desarrollar una extensión es asegurarse de tener instalados VS Code y Node.js en tu entorno local, para luego utilizar npm para instalar Yeoman y el Generador de Extensiones de VS Code, y así generar rápidamente el esqueleto para el desarrollo de la extensión:

```
npm install -g yo generator-code
```

Una vez instalado, ejecuta el comando para crear una nueva extensión:

```
yo code
```

Cuando te solicite elegir el tipo de extensión, puedes seleccionar "Nueva Extensión (TypeScript)" o cualquier otro tipo según tus preferencias.

Dentro del marco generado automáticamente, hay dos archivos importantes con nombres y funciones específicas:

- src/extension.ts: Punto de entrada principal y lógica de la extensión.
- package.json: Define los metadatos y dependencias de la extensión.

## Desarrollo de la extensión

## Pruebas de la extensión

Para ejecutar y depurar la extensión, simplemente presiona `F5` en VS Code. En este ejemplo, al abrir un archivo Markdown en la ventana de depuración, podrás probar si la extensión puede renderizar una página de panel.

## Empaquetar y publicar la extensión

Para empaquetar la extensión, necesitarás instalar la herramienta vsce:

```
npm install -g vsce
```

Luego, utiliza `vsce package` para empaquetar la extensión.

(en proceso)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.