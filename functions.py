import streamlit as st

# Function to create the prompt for the decks generation
def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst extract and present information from {text_file}. Do the following tasks and answer always in Spanish.
    Task 1: Identify the "Razón Social"
    Task 2: Identify the "Nit"
    Task 3: Identify the "Domicilio principal"
    Task 4: Identify the "Matrícula No."
    Task 5: Identify the "Teléfono comercial 1:"
    Task 6: Identify the "Teléfono comercial 2:" 
    Task 7: Identify the "Página web:"
    Task 8: Identify the "Correo electrónico:"
    Task 9: Identify the "OBJETO SOCIAL:"
    Task 10: Identify the "REPRESENTANTE LEGAL PRINCIPAL"
    Task 11: Identify the "REPRESENTANTE LEGAL SUPLENTE"
    Task 12: Identify the "Actividad principal código CIIU:"
    Task 13: Identify the "Actividad secundaria código CIIU:"
    
    Here is an example of a text that you may receive, never use this text for your answers this is just an example: "Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------CON FUNDAMENTO EN LA MATRÍCULA E INSCRIPCIONES EFECTUADAS EN EL REGISTRO
MERCANTIL, LA CÁMARA DE COMERCIO CERTIFICA:
NOMBRE, IDENTIFICACIÓN Y DOMICILIO
Razón social:

MIND MEDELLIN S.A.S

Sigla:

No reportó

Nit:

901696738-1

Domicilio principal:

MEDELLÍN, ANTIOQUIA, COLOMBIA
MATRÍCULA

Matrícula No.:
Fecha de matrícula:
Último año renovado:
Fecha de renovación:
Grupo NIIF:

21-752137-12
23 de Marzo de 2023
2023
23 de Marzo de 2023
Entidades que se clasifiquen según
el Artículo No. 2 de la resolución
414 del 2014, según la Contaduría
General de la Nación (CGN).

CONDICIÓN DE PEQUEÑA EMPRESA JOVEN
ESTE COMERCIANTE CUMPLE CON LA CONDICIÓN DE PEQUEÑA EMPRESA JOVEN DE
ACUERDO CON LO ESTABLECIDO EN LA LEY 1780 DE 2016 Y EL DECRETO 639 DE
2017.
UBICACIÓN
Dirección del domicilio principal: Carrera 37 No. 8 A 32
Municipio:
MEDELLÍN, ANTIOQUIA, COLOMBIA
Correo electrónico:
saris1127@gmail.com
Teléfono comercial 1:
3052952099
Teléfono comercial 2:
No reportó
Teléfono comercial 3:
No reportó
Página web:
No reportó
Dirección para notificación judicial: Carrera 37 No. 8 A 32
Municipio:
MEDELLÍN, ANTIOQUIA, COLOMBIA
Página: 1 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------Correo electrónico de notificación:
Teléfono para notificación 1:
Teléfono para notificación 2:
Teléfono para notificación 3:

saris1127@gmail.com
3052952099
No reportó
No reportó

La persona jurídica MIND MEDELLIN S.A.S SI autorizó para recibir
notificaciones personales a través de correo electrónico, de conformidad
con lo establecido en los artículos 291 del Código General del Proceso y
67 del Código de Procedimiento Administrativo y de lo Contencioso
Administrativo
CONSTITUCIÓN
Por Documento Privado del 22 de Marzo de 2023 de la Accionista,
inscrito(a) en esta Cámara de Comercio el 23 de marzo de 2023, con el
No.9911 del Libro IX, se constituyó la Sociedad de naturaleza Comercial
denominada MIND MEDELLIN S.A.S
TERMINO DE DURACIÓN
La
persona
indefinida.

jurídica

no

se

encuentra

disuelta

y

su

duración

es

OBJETO SOCIAL
El objeto social de la compañía es de naturaleza comercial y consiste en
la realización de toda actividad comercial y civil lícita en el país y
en el extranjero sin reserva ni limitación alguna interviniendo en forma
individual o en asociación con otras personas jurídicas o naturales.
No obstante, lo anterior la compañía se dedicará principalmente a las
siguientes actividades:
a) Venta,
alimentos;

comercialización,

promoción

y

distribución

de

bebidas y

b) Prestar espacios para reuniones y negocios.
PARÁGRAFO: Para la realización del objeto social la compañía podrá
llevar
a cabo, en general, todas las operaciones, de cualquier
naturaleza que ellas fueren, relacionadas con el objeto mencionado, así
como cualesquiera actividades similares, conexas o complementarias o que
Página: 2 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------permitan facilitar o desarrollar el comercio o la industria de la
sociedad. En este sentido, la compañía podrá ejecutar las siguientes
actividades que se nombran de forma meramente enunciativa: Adquirir
todos los activos fijos, muebles o inmuebles, que sean necesarios para
el desarrollo de los negocios sociales; gravar o limitar el dominio de
sus activos fijos, sean muebles o inmuebles, y enajenarlos cuando por
razones de necesidad o conveniencia fuere aconsejable; edificar locales
para uso de sus propios establecimientos, sin perjuicio de que pueda
accesoriamente enajenar pisos, locales o departamentos, darlos en
arrendamiento o explotarlos en otra forma conveniente; administrar,
establecer y explotar empresas comerciales de distribución, ventas o
fabricación de elementos o bienes que se requieran en el desarrollo de
sus actividades; concurrir a la constitución de nuevas sociedades o
ingresar como socio a las ya existentes, así como la realización e
intervención en procesos de fusión y escisión de sociedades.
CAPITAL
Valor
No. de acciones
Valor Nominal

:
:
:

CAPITAL AUTORIZADO
$500.000.000,00
50.000,00
$10.000,00

Valor
No. de acciones
Valor Nominal

:
:
:

CAPITAL SUSCRITO
$50.000.000,00
5.000,00
$10.000,00

Valor
No. de acciones
Valor Nominal

:
:
:

CAPITAL PAGADO
$50.000.000,00
5.000,00
$10.000,00
REPRESENTACIÓN LEGAL

La administración y representación legal de la sociedad está en cabeza
del representante legal, quien tendrá suplente.
La representación legal puede ser ejercida por personas naturales o
jurídicas,
la Asamblea General de Accionistas, designara a los
representantes legales por el período que libremente determine o en
forma indefinida, si así lo dispone, y sin perjuicio de que los
Página: 3 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------nombramientos sean revocados libremente en cualquier tiempo.
FACULTADES Y LIMITACIONES DEL REPRESENTANTE LEGAL
FACULTADES DEL REPRESENTANTE LEGAL: El representante legal pueden
celebrar o ejecutar todos los actos y contratos comprendidos en el
objeto social o que se relacionen directamente con la existencia y
funcionamiento de la sociedad.
NOMBRAMIENTOS
REPRESENTANTES LEGALES
Por Documento Privado del 22 de marzo de 2023, de la Accionista,
inscrito(a) en esta Cámara de Comercio el 23 de marzo de 2023, con el
No.9911 del Libro IX, se designó a:
CARGO
REPRESENTANTE LEGAL

NOMBRE
SARA LUZ ESTRADA LOPERA

IDENTIFICACION
C.C. 1.152.201.543

REPRESENTANTE LEGAL
SUPLENTE

NATALIA MARIA SALAZAR
HENAO

C.C. 43.597.466

REFORMAS DE ESTATUTOS
Que hasta la fecha la Sociedad no ha sido reformada.
RECURSOS CONTRA LOS ACTOS DE INSCRIPCIÓN
De conformidad con lo establecido en el Código de Procedimiento
Administrativo y de lo Contencioso Administrativo y la Ley 962 de 2005,
los actos administrativos de registro, quedan en firme dentro de los
diez (10) días hábiles siguientes a la fecha de inscripción, siempre que
no sean objeto de recursos. Para estos efectos, se informa que para la
Cámara de Comercio de Medellín para Antioquia, los sábados NO son días
hábiles.
Una vez interpuestos los recursos, los actos administrativos recurridos
quedan en efecto suspensivo, hasta tanto los mismos sean resueltos,
conforme
lo
prevé el artículo 79 del Código de Procedimiento
Administrativo y de los Contencioso Administrativo.

Página: 4 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------A la fecha y hora de expedición de este certificado, NO se encuentra en
curso ningún recurso.
SITUACIÓN(ES) DE CONTROL / GRUPO EMPRESARIAL
SITUACION DE CONTROL
SITUTACIÓN DE CONTROL
MATRIZ: ESTRADA LOPERA SARA LUZ
DOMICILIO: MEDELLÍN - COLOMBIANA
ACTIVIDAD: PREPARACIÓN Y EXPENDIO DE ALIMENTOS, SERVICIO A LA
MESA
DOCUMENTO: FORMATO DECLARA O REHÚSA SITUACIÓN DE CONTROL DEL 04
DE AGOSTO DE 2022
DATOS INSCRIPCION: Libro 9 Nro. 29390 18/08/2022
MODIFICACION: FORMATO DECLARA O REHÚSA SITUACIÓN DE CONTROL DEL
22 DE MARZO DE 2023
DATOS INSCRIPCION: Libro 9 Nro. 9912 23/03/2023
CONTROLA DIRECTAMENTE A:
734893 12 MCONSTRUCTION, S.A.S.
DOMICILIO: MEDELLÍN - COLOMBIANA
Subordinada
PRESUPUESTO: ARTICULO 261-NUMERAL 1 DEL CODIGO DE COMERCIO:
PROPIEDAD DEL 100% DE LAS ACCIONES QUE COMPONEN EL CAPITAL DE
SOCIEDAD.
ACTIVIDAD: ACTIVIDADES INMOBILIARIAS CON BIENES PROPIOS O
ARRENDADOS
DOCUMENTO: FORMATO DECLARA O REHÚSA SITUACIÓN DE CONTROL DEL 04
DE AGOSTO DE 2022
DATOS INSCRIPCION: Libro 9 Nro. 29390 18/08/2022
752137 12 MIND MEDELLIN S.A.S
DOMICILIO: MEDELLÍN - COLOMBIANA
Subordinada
PRESUPUESTO: ARTICULO 261-NUMERAL 1 DEL CODIGO DE COMERCIO:
PROPIEDAD DEL 100% DE LAS ACCIONES QUE COMPONEN EL CAPITAL DE
LA SOCIEDAD
ACTIVIDAD: PREPARACIÓN Y EXPENDIO DE ALIMENTOS, SERVICIO A LA
MESA
Página: 5 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------DOCUMENTO: FORMATO DECLARA O REHÚSA SITUACIÓN DE CONTROL DEL 22
DE MARZO 22 DE 2023
DATOS INSCRIPCION: Libro 9 Nro. 9912 23/03/2023
CLASIFICACIÓN DE ACTIVIDADES ECONÓMICAS - CIIU
Actividad principal código CIIU:

5611

ESTABLECIMIENTO(S) DE COMERCIO
A nombre de la persona jurídica figura matriculado en esta Cámara de
Comercio el siguiente establecimiento de comercio/sucursal o agencia:
Nombre:
Matrícula No.:
Fecha de Matrícula:
Ultimo año renovado:
Categoría:
Dirección:
Municipio:

MIND MEDELLIN SAS
21-767981-02
23 de Marzo de 2023
2023
Establecimiento-Principal
Carrera 37 No. 8 A 32
MEDELLÍN, ANTIOQUIA, COLOMBIA

SI
DESEA
OBTENER
INFORMACIÓN
DETALLADA
DE LOS ANTERIORES
ESTABLECIMIENTOS
DE COMERCIO O DE AQUELLOS MATRICULADOS EN UNA
JURISDICCIÓN DIFERENTE A LA DEL PROPIETARIO, DEBERÁ SOLICITAR EL
CERTIFICADO DE MATRÍCULA MERCANTIL DEL RESPECTIVO ESTABLECIMIENTO DE
COMERCIO.
LA INFORMACIÓN CORRESPONDIENTE A LOS ESTABLECIMIENTOS DE COMERCIO,
AGENCIAS Y SUCURSALES, QUE LA PERSONA JURÍDICA TIENE MATRICULADOS EN
OTRAS
CÁMARAS
DE
COMERCIO
DEL PAÍS, PODRÁ CONSULTARLA EN
WWW.RUES.ORG.CO.
SE RECOMIENDA VERIFICAR EL PORTAL WWW.GARANTIASMOBILIARIAS.COM.CO DONDE
PUEDEN
OBRAR
INSCRIPCIONES
ADICIONALES RELATIVAS A GARANTIAS
MOBILIARIAS, CONTRATOS QUE GARANTICEN OBLIGACIONES O LIMITACIONES DE LA
PROPIEDAD.
TAMAÑO DE EMPRESA
De conformidad con lo previsto en el artículo 2.2.1.13.2.1 del decreto
1074 de 2015 y la Resolución 2225 de 2019 del DANE el tamaño de la
Página: 6 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
-----------------------------------------------------------------------empresa es micro.
Lo anterior de acuerdo a la información reportada por el matriculado o
inscrito en el formulario RUES:
Ingresos por actividad ordinaria $0.00
Actividad económica por la que percibió mayores ingresos en el período CIIU: 5611
INFORMACIÓN COMPLEMENTARIA
Este certificado refleja la situación jurídica registral de la sociedad,
a la fecha y hora de su expedición.
Este certificado cuenta con plena validez jurídica según lo dispuesto en
la ley 527 de 1999. En él se incorporan tanto la firma mecánica que es
una representación gráfica de la firma del Secretario de la Cámara de
Comercio de Medellín para Antioquia, como la firma digital y la
respectiva estampa cronológica, las cuales podrá verificar a través de
su aplicativo visor de documentos PDF.
Si usted expidió el certificado a través de la plataforma virtual, puede
imprimirlo con la certeza de que fue expedido por la Cámara de Comercio
de Medellín para Antioquia. La persona o entidad a la que usted le va a
entregar
el certificado puede verificar su contenido de manera
ilimitada, durante 60 días calendario contados a partir del momento de
su expedición, ingresando a www.certificadoscamara.com y digitando el
código de verificación que se encuentra en el encabezado del presente
documento. El certificado a validar corresponde a la imagen y contenido
del certificado creado en el momento en que se generó en las taquillas o
a través de la plataforma virtual de la Cámara.
........................................................................
........................................................................
........................................................................
........................................................................
........................................................................
........................................................................
........................................................................
Página: 7 de 8

Cámara de Comercio de Medellín para Antioquia
CERTIFICADO DE EXISTENCIA Y REPRESENTACIÓN LEGAL
Fecha de expedición: 11/07/2023 - 2:30:06 PM
Recibo No.: 0025227835

Valor: $00

CÓDIGO DE VERIFICACIÓN: acibkilLjlFsklib
-----------------------------------------------------------------------Verifique el contenido y confiabilidad de este certificado, ingresando a
www.certificadoscamara.com y digite el respectivo código, para que
visualice
la
imagen
generada al momento de su expedición. La
verificación se puede realizar de manera ilimitada, durante 60 días
calendario, contados a partir de la fecha de su expedición.
------------------------------------------------------------------------

Página: 8 de 8

" and this is the answer you should provide: 
Razón Social: UNERGY S.A.S.
Nit: 901372693-8
Domicilio principal: MEDELLÍN, ANTIOQUIA, COLOMBIA
Matrícula No.: 21-669758-12
Teléfono comercial 1: 3155000797
Teléfono comercial 2: 3186388750
Página web: No reportó
Correo electrónico: administracion@unergy.io
OBJETO SOCIAL: Toda actividad civil o comercial, lícita.
REPRESENTANTE LEGAL PRINCIPAL: EDUARDO ANDRES OSPINA SERRANO
REPRESENTANTE LEGAL SUPLENTE: NICOLAS  VILLEGAS ECHAVARRIA
Actividad principal código CIIU: 3511
Actividad secundaria código CIIU: 6201
'''


    return prompts