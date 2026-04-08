# 📘 Tarefa: Construindo APIs REST com o framework FastAPI

## 🎯 Objective

Aprenda a construir APIs REST robustas usando FastAPI, incluindo operações CRUD, validação de dados e documentação automática de API.

## 📝 Tasks

### 🛠️ Criar uma API Básica com Endpoints

#### Descrição
Implemente uma API REST básica com FastAPI que predefina um modelo de dados simples (por exemplo, um item ou tarefa) e crie endpoints para operações fundamentais.

#### Requisitos
O programa completo deve:

- Importar e configurar FastAPI corretamente
- Definir um modelo de dados usando Pydantic (por exemplo, `Item` ou `Task`)
- Criar um endpoint GET `/items/` que retorna uma lista de itens
- Criar um endpoint GET `/items/{item_id}` que retorna um item específico
- Criar um endpoint POST `/items/` que adiciona um novo item
- Retornar dados no formato JSON com status codes apropriados


### 🛠️ Adicionar Validação e Tratamento de Erros

#### Descrição
Implemente validação de dados usando Pydantic e adicione tratamento de erros com mensagens significativas.

#### Requisitos
O programa completo deve:

- Validar os dados de entrada usando Pydantic com tipos e restrições apropriadas
- Retornar status code 404 quando um item não for encontrado
- Retornar status code 400 para dados inválidos
- Incluir mensagens de erro descritivas
- Testar os endpoints com diferentes entradas para verificar o comportamento


### 🛠️ Implementar Operações Update e Delete

#### Descrição
Expanda a API para incluir endpoints para atualizar e deletar itens, completando as operações CRUD.

#### Requisitos
O programa completo deve:

- Criar um endpoint PUT `/items/{item_id}` para atualizar um item existente
- Criar um endpoint DELETE `/items/{item_id}` para remover um item
- Validar que o item existe antes de atualizar ou deletar
- Retornar as confirmações apropriadas (item atualizado, deletado, ou não encontrado)
- Demonstrar todas as operações CRUD funcionando corretamente
