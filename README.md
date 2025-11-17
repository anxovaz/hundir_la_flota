```mermaid
flowchart TB
    A(["Inicio"]) --> n1["contador = 0"]
    n1 --> n2["i &gt; len(lista)"]
    n2 --> n3["j &gt; len(i)"] & n15["Devolver contador"]
    n3 --> n6["j != 0"] & n14["i += 1"]
    n6 --> n9["contador += 1"] & n7["j += 1"]
    n9 --> n8["j += 1"]
    n14 L_n14_n2_0@--> n2
    n8 L_n8_n3_0@--> n3
    n7 L_n7_n3_0@--> n3
    n15 --> n16(["Fin"])
    n1@{ shape: rect}
    n2@{ shape: diam}
    n3@{ shape: diam}
    n15@{ shape: rect}
    n6@{ shape: diam}
    n14@{ shape: rect}
    n9@{ shape: rect}
    n7@{ shape: rect}
    n8@{ shape: rect}
    L_n14_n2_0@{ curve: linear } 
    L_n8_n3_0@{ curve: linear } 
    L_n7_n3_0@{ curve: linear }

```