# Canabinote — LP do paciente

Landing page responsiva para revisão e aprovação da Canabinote.

## Estrutura

- `dist/`: site estático pronto para publicação.
- `build.py` e `sections.py`: geração do HTML a partir da copy em `dist/copy.json`.
- `dist/styles.css`: estilos responsivos.
- `dist/app.js`: interações e acessibilidade.
- `CREDITOS.md`: fontes e créditos das imagens.

## Edição

Edite os textos em `dist/copy.json` e, para mudanças estruturais, `sections.py` ou `build.py`. Execute `python build.py` para atualizar o HTML. CSS e JavaScript são editados diretamente. Não é necessário instalar pacotes.

## Visualização local

Execute `python -m http.server 4173 --directory dist` e abra http://localhost:4173/.

## Publicação

A pasta `dist` é publicada na branch `gh-pages`. A branch `main` mantém os arquivos de edição. Alterações futuras podem ser publicadas no mesmo endereço.

A página é informativa. Os botões encaminham para os destinos oficiais fornecidos pela Canabinote. Fotografias de banco são ilustrativas e não representam depoimentos de pacientes.
