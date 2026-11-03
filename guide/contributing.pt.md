---
title: Trabalhando neste repositório
---

# Trabalhando neste repositório

As 179 configs do `configs.zip` são **geradas a partir de um pequeno conjunto de
perfis**, e não guardadas uma por uma. As ferramentas que fazem isso (o
construtor, as tabelas de hardware e o teste de equivalência que prova que uma
mudança num perfil não alterou o que alguém baixa) estão documentadas no
[tools/README.md](https://github.com/yusufklncc/Hackintosh-for-All-Computers/blob/main/tools/README.md)
(em inglês).

```
python3 tools/selftest.py                          tudo, incluindo este site
python3 tools/build.py --catalogue                 todas as configs publicadas
python3 tools/build.py --name "Laptop/HP/009 - Laptop - Kaby Lake"
```

## O que uma mudança precisa aguentar

Nada aqui é aceito só porque parece certo. Toda tabela diz de onde veio, e a
tela **Sobre** do programa diz isso em voz alta: derivado, medido, citado,
relatado, ou sem fonte nenhuma, dito claramente.

- Um dispositivo apontado como compatível cita o kext que o atende, lido do
  próprio `Info.plist` desse kext.
- Uma frase sobre o comportamento de um hardware que nenhum documento oficial
  afirma vai em `data/field.toml`, com o nome de quem observou e exatamente o
  que a pessoa viu. *"Não funciona"* não é uma entrada; *"instala, mas a
  aceleração de vídeo não tem como funcionar"* é.
- Uma mudança de config precisa passar no teste de equivalência, que gera de
  novo todas as configs publicadas e compara com um catálogo de hashes.

## Editando este guia

Cada página tem um ícone de lápis no canto superior direito que abre ela no
GitHub.

O site fica em `guide/`, e toda página existe em três versões: `bios.md` em
inglês, `bios.tr.md` em turco e `bios.pt.md` em português. O selftest falha se
faltar alguma delas, então uma página adicionada num idioma não consegue ser
publicada sem as outras.

```
pip install -r guide/requirements.txt
mkdocs serve                                       prévia em localhost:8000
```

## A versão da release

A tag acompanha a **versão do OpenCore** incluída no repositório: `v1.0.7` quer
dizer OpenCore 1.0.7. Ela nunca sobe por causa de funcionalidades novas. Quando
o OpenCore não mudou e uma correção precisa sair, a release é publicada de novo
na mesma tag; veja o
[docs/RELEASING.md](https://github.com/yusufklncc/Hackintosh-for-All-Computers/blob/main/docs/RELEASING.md)
(em inglês).
