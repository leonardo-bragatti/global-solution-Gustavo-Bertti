from database.models import Enfermeiro, Tecnico, Equipe, Nas,Paciente, EquipeTecnicoAssociation
from database.__init__  import get_db
from datetime import datetime

def cadastrar_enfermeiro(nome, coren, senha):
    enfermeiro = Enfermeiro(nome=nome, coren=coren, senha=senha)
    
    with get_db() as db:
        db.add(enfermeiro)
        db.commit()

        # Atualiza a instância do enfermeiro para garantir que está associada à sessão
        db.refresh(enfermeiro)

        print("Enfermeiro cadastrado com sucesso!")

    # Retorna o ID do enfermeiro após o commit
    return enfermeiro.id

def menu_cadastroEnfermeiro():
    print("\n=== Cadastro de Enfermeiro ===")
    nome = input("Digite o nome do enfermeiro: ")
    coren = int(input("Digite o COREN do enfermeiro: "))
    senha = input("Digite a senha do enfermeiro: ")

    id_enfermeiro = cadastrar_enfermeiro(nome, coren, senha)

    # Retorna o ID do enfermeiro
    return id_enfermeiro
def cadastrar_tecnico(nome, coren):
    tecnico = Tecnico(nome=nome, coren=coren)

    with get_db() as db:
        db.add(tecnico)
        db.commit()

        # Atualiza a instância do técnico para garantir que está associada à sessão
        db.refresh(tecnico)

        print("Técnico cadastrado com sucesso!")

    # Retorna a instância do técnico após o commit
    return tecnico

def menu_cadastroTecnico():
    print("\n=== Cadastro de Técnico ===")
    nome = input("Digite o nome do técnico: ")
    coren = input("Digite o COREN do técnico: ")

    # Retorna a instância do técnico a partir da função cadastrar_tecnico
    tecnico = cadastrar_tecnico(nome, coren)

    # Retorna a instância do técnico
    return tecnico

def cadastrar_equipe():
    print("\n=== Cadastro de Equipe ===")
    nome_equipe = input("Digite o nome da equipe: ")
    senha_equipe = input("Digite a senha da equipe: ")

    # Obtém o ID do enfermeiro a partir da função menu_cadastroEnfermeiro
    id_enfermeiro = menu_cadastroEnfermeiro()

    # Adiciona a equipe ao banco de dados
    with get_db() as db:
        equipe = Equipe(nome_equipe=nome_equipe, senha_equipe=senha_equipe, enfermeiro_id=id_enfermeiro)
        db.add(equipe)
        db.commit()

        # Agora, equipe.id está disponível
        print(f"Equipe cadastrada com sucesso! ID: {equipe.id}")

        # Adiciona os técnicos à equipe
        tecnicos = [menu_cadastroTecnico() for _ in range(5)]
        for tecnico in tecnicos:
            equipe_tecnico_association = EquipeTecnicoAssociation(equipe_id=equipe.id, tecnico_id=tecnico.id)
            db.add(equipe_tecnico_association)
        db.commit()

    print("Técnicos adicionados à equipe com sucesso!")

def cadastrar_paciente():
    print("\n=== Cadastro de Paciente ===")
    cpf = input("Digite o CPF do paciente: ")
    nome = input("Digite o nome do paciente: ")
    data_nascimento_str = input("Digite a data de nascimento do paciente (no formato dd/mm/yyyy): ")
    idade = input("Digite a idade do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
    # Converta a string de data para um objeto datetime
    

    # Converta a data para o formato aceito pelo Oracle
    

    paciente = Paciente(cpf=cpf, nome=nome, dataNascimento=data_nascimento, idade=idade, telefone=telefone)

    try:
        with get_db() as db:
            # Adicione o paciente à sessão e depois faça commit
            db.add(paciente)
            db.commit()

            paciente_id = paciente.id
            

        print("Paciente cadastrado com sucesso! ID:", paciente_id)
        return paciente_id
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")

            
def cadastrar_nas():
    print("\n=== Cadastro de NAS ===")
    print("\n=== Monitorização e Controles ===")
    a1 = float(input('Sinais vitais horários, cálculo e registro regular do balanço hídrico.valor max = 4.5:'))
    b1 = float(input('Presença à beira do leito e observação contínua ou ativa por 2 horas ou mais em algum plantão por razões de segurança, gravidade ou terapia, como ventilação não invasiva, desmame, agitação, confusão mental, posição prona, procedimentos de doação de órgãos, preparo e administração de fluidos ou medicação, auxílio em procedimentos específicos.valor max = 12.1:'))
    c1 = float(input('Presença à beira do leito e observação contínua ou ativa por 4 horas ou mais em algum plantão por razões de segurança, gravidade ou terapia, como os exemplos acima.valor max = 19.6:'))
    a2 = float(input('Investigações Laboratoriais: Bioquímicas e Microbiológicas.valor max = 4.3:'))
    a3 = float(input('Medicação, exceto drogas vasoativas.valor max = 5.6:'))
    print("\n === Procedimentos de Higiene ===")
    a4 = float(input('Realização de procedimentos de higiene, como curativos de feridas e cateteres intravasculares, troca de roupa de cama, higiene corporal do paciente em situações especiais (incontinência, vômito, queimaduras, feridas com secreção, curativos cirúrgicos complexos com irrigação), procedimentos especiais (por exemplo: isolamentos) e etc.valor max = 4.1:'))
    b4 = float(input('Realização de procedimentos de higiene que durem mais do que duas horas em algum plantão.valor max = 16.5:'))
    c4 = float(input('Realização de procedimentos de higiene que durem mais do que quatro horas em algum plantão.valor max = 20:'))
    a5 = float(input('Cuidados com Drenos. Todos exceto (sonda gástrica).valor max = 1.8'))
    print("\n === Mobilização e Posicionamento, incluindo procedimentos como mudanças de decúbito, mobilização do paciente, transferência da cama para cadeira: mobilização dos pacientes em equipe (por exemplo, o paciente imóvel, tração, posição prona) ===")
    a6 = float(input('Realização do(s) procedimento(s) até três vezes em 24 horas.valor max = 5.5:'))
    b6 = float(input('Realização do(s) procedimento(s) mais do que três vezes em 24 horas ou com dois enfermeiros em qualquer frequência.valor max = 12.4:'))
    c6 = float(input('Realização do(s) procedimento(s) com três ou mais enfermeiras em qualquer frequência.valor max = 17:'))
    print("\n === Suporte e Cuidados aos Familiares e Pacientes, incluindo procedimentos como telefonemas, entrevistas, aconselhamento. Frequentemente, o suporte e cuidados aos familiares ou aos pacientes permitem que a equipe continue com outras atividades de enfermagem, por exemplo, comunicação com o paciente durante o procedimento de higiene, comunicação com os familiares enquanto presente à beira do leito observando o paciente ===")
    a7 = float(input('Suporte e cuidados aos familiares e pacientes que requerem dedicação exclusiva por cerca de uma hora em algum plantão, como explicar condições clínicas, dar conforto e lidar com a dor e a angústia, enfrentando circunstâncias familiares difíceis.valor max = 4:'))  
    b7 = float(input('Suporte e cuidados aos familiares e pacientes que requerem dedicação exclusiva por três horas ou mais em algum plantão, como em casos de morte, circunstâncias especiais, por exemplo, grande número de familiares, problemas de linguagem, familiares hostis.valor max = 32:'))
    print("\n === Tarefas Administrativas e Gerenciais ===")    
    a8 = float(input('Realização de tarefas de rotina, como procedimentos de dados clínicos, solicitação de exames, troca de informações profissionais, por exemplo, passagem de plantão, visitas clínicas.valor max = 4.2:'))
    b8 = float(input('Realização de tarefas administrativas e gerenciais que requerem dedicação integral por cerca de duas horas em algum plantão, como atividades de pesquisa, aplicação de protocolos, procedimentos de admissão e alta.valor max = 23.2:'))
    c8 = float(input('Realização de tarefas administrativas e gerenciais que requerem dedicação integral por cerca de 4 horas ou mais de tempo em algum plantão, como em casos de morte e procedimentos de doação de órgão, coordenação com outras disciplinas.valor max = 30:'))
    print("\n=== Suporte Ventilatório ===")
    a10 = float(input('Suporte Respiratório, qualquer forma de ventilação mecânica assistida com ou sem pressão, com ou sem tubo endotraqueal, oxigênio suplementar por qualquer método.valor max = 1.4:')) 
    a11 = float(input('Cuidado com Vias Aéreas Artificiais, tubo Endotraqueal ou Cânula de traqueostomia.valor max = 1.8:'))
    a12 = float(input('Tratamento para Melhora da Função Pulmonar, fisioterapia torácica, espirometria estimulada, terapia inalatória, aspiração endotraqueal.valor max = 4.4:'))
    print("\n === Suporte CardioVascular ===")
    a13 = float(input('Medicação Vasoativa, independente do tipo.valor max = 1.2:'))
    a14 = float(input('Reposição Intravenosa de Grandes Perdas de Fluidos, administração de fluidos maior de 3 bm2/dia, independente do tipo de fluido administrado.valor max = 2.5:'))
    a15 = float(input('Monitoração do Átrio Esquerdo, cateter da artéria pulmonar com ou sem medida do débito cardíaco.valor max = 1.7:'))
    a16 = float(input('Reanimação Cardiorrespiratória nas últimas 24 horas, excluindo soco precordial.valor max = 7.1:'))
    print("\n === Suporte Renal ===")
    a17 = float(input('Técnica de Hemofiltração, técnica dialítica.valor max = 7.7:'))
    a18 = float(input('Medida Quantitativa do Débito Urinário, por exemplo, por sonda vesical de demora.valor max = 7:'))
    print("\n === Suporte Neurológico ===")
    a19 = float(input('Medida da Pressão Intracraniana.valor max = 1.6:'))
    print("\n === Suporte Metabólico ===")
    a20 = float(input('Tratamento da Acidose/Alcalose Metabólica Complicada.valor max = 1.3:'))
    a21 = float(input('Nutrição Parenteral Total.valor max = 2.8:'))
    a22 = float(input('Alimentação Enteral por Sonda Gástrica ou outra via gastrointestinal, por exemplo, jejunostomia.valor max = 1.3:'))
    print("\n === Intervenções Específicas ===")
    a23 = float(input('Alimentação Específica na Unidade de Terapia Intensiva, intubação endotraqueal, inserção de marca-passo, cardioversão, endoscopia, cirurgia de emergência nas últimas 24 horas, lavagem gástrica não induzida, intervenções de rotina sem consciência direta para as condições clínicas do paciente, como radiografias, ecografias, eletrocardiogramas, curativos ou inserção de cateteres arteriais.valor max = 2.8:'))
    a24 = float(input('Intervenções Específicas Fora da Unidade de Terapia Intensiva, procedimentos diagnósticos ou cirúrgicos.valor max = 1.9:'))

    paciente_id = cadastrar_paciente()
    total = a1 + b1 + c1 + a2 + a3 + a4 + b4 + c4 + a5 + a6 + b6 + c6 + a7 + b7 + a8 + b8 + c8 + a10 + a11 + a12 + a13 + a14 + a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 + a24
    complexidade = ''
    if total < 50:
        complexidade = 'Baixa'
    elif total > 49 and total < 100:
         complexidade = 'Media'
    elif total > 100:
        complexidade = 'Alta'
    
    nas_instance = Nas(nota_nas=total, complexidade=complexidade, paciente_id=paciente_id)

    try:
            # Salva a instância no banco de dados
            with get_db() as db:
                db.add(nas_instance)
                db.commit()

            print("NAS cadastrado com sucesso!")
    except Exception as e:
            print(f"Erro ao cadastrar NAS: {e}")
    
    


def realizar_login():
    nome = input("Digite o nome da equipe: ")
    senha = input("Digite a senha: ")

    with get_db() as db:
        equipe = db.query(Equipe).filter_by(nome_equipe=nome, senha_equipe=senha).first()
        if equipe:
            print(f"Login bem-sucedido para a equipe {equipe.nome_equipe}!")
        else:
            print("Credenciais inválidas")

def mostrar_nas_paciente(paciente_id):
    with get_db() as db:
        # Verifica se o paciente existe
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()

        if paciente:
            # Busca os NAS associados ao paciente
            nas_list = db.query(Nas).filter(Nas.paciente_id == paciente_id).all()

            if nas_list:
                print(f"\nNAS do Paciente {paciente.nome}:")
                for nas in nas_list:
                    print(f"ID do NAS: {nas.id}")
                    print(f"Nota NAS: {nas.nota_nas}")
                    print(f"Complexidade: {nas.complexidade}")
                    print("\nDetalhes do NAS:")
                   
                    
            else:
                print("Este paciente não possui NAS cadastrados.")
        else:
            print("Paciente não encontrado.")