# padrao_desenvolvimento_Builder
Trabalho sobre o padrão de desenvolvimento Builder

Principais vantagens do padrão Builder:

1. Criação de objetos complexos de forma controlada

Permite construir objetos que possuem muitos parâmetros opcionais ou obrigatórios, evitando construtores gigantes ("telescoping constructors").

2. Código mais legível e expressivo

A criação passo a passo (métodos encadeados) torna o código mais fácil de entender:

python => CarroBuilder().set_marca("Ford").set_modelo("Fiesta").build()

3. Facilita manutenção e evolução

Adicionar novos atributos exige apenas incluir novos métodos no Builder, sem quebrar código já existente.

4. Suporta diferentes representações do mesmo objeto

É possível ter múltiplos builders para criar objetos de diferentes maneiras (útil para saídas diferentes: JSON, objetos complexos, etc.).

5. Encapsula lógica de validação

O build() pode validar dados antes de criar o objeto final, garantindo consistência.

6. Evita necessidade de múltiplos construtores

Ao invés de vários __init__ com combinações de parâmetros, o Builder organiza tudo em um fluxo só.

Pontos fracos do padrão Builder:

1. Pode adicionar complexidade extra

Para objetos simples, usar Builder pode ser exagero e desnecessário.

2. Aumenta a quantidade de código

É preciso criar a classe Builder, métodos setters, lógica de build, etc.

3. Pode ser menos “Pythonico” se não for bem projetado

Python já oferece alternativas mais simples (como @dataclass com valores padrão), tornando o Builder menos comum se comparado a linguagens como Java.

4. Risco de objetos parcialmente construídos

Se o programador esquecer de chamar build(), pode haver interpretações erradas ou fluxo incompleto — especialmente se campos obrigatórios não forem bem validados.

5. Pode dificultar a autocompletação e tipagem em IDEs

Builders muito dinâmicos podem gerar cadeias de métodos difíceis de tipar estaticamente, embora isso possa ser mitigado com boas anotações de tipo.

Conclusão:

O padrão Builder é extremamente útil quando você precisa construir objetos complexos, configuráveis e com muitos parâmetros, principalmente quando há combinações variadas de campos opcionais e obrigatórios. Ele melhora a legibilidade, organização e manutenibilidade do código.

Por outro lado, ele pode introduzir complexidade desnecessária em projetos menores ou para objetos simples. Em Python, devido a recursos como @dataclass e parâmetros opcionais, o uso do Builder é menos frequente — mas continua muito valioso em cenários onde a criação de objetos deve ser clara, segura e extensível.


