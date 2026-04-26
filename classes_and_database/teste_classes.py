from platform_class import Platform  
db_name = "novadatabase5.db"

print("\n[Teste 1] Leitura SQL e Amostra de Dados:")
Platform.read(db_name)
for p in list(Platform.obj.values())[:7]: 
    print(p)


print("\n[Teste 2] Validação de Quantidade:")
print(f"Total de Plataformas carregadas do SQL: {len(Platform.obj)}")

# %%

from certificate import Certificate
db_name = "novadatabase5.db"


print("\n[Teste 1] Leitura SQL e Amostra de Dados:")
Certificate.read(db_name)
for c in list(Certificate.obj.values())[:7]:
    print(c)

print("\n[Teste 2] Validação de Quantidade:")
print(f"Total de Certificados carregados do SQL: {len(Certificate.obj)}")


# %%

from course import Course
db_name = "novadatabase5.db"


print("\n[Teste 1] Leitura SQL e Amostra de Dados:")
Course.read(db_name)
for curso in list(Course.obj.values())[:7]:
    print(curso)


print("\n[Teste 2] Validação de Quantidade:")
print(f"Total de Cursos carregados do SQL: {len(Course.obj)}")

# %%

from transaction import Trans  
db_name = "novadatabase5.db"


print("\n[Teste 1] Leitura SQL e Amostra de Dados:")
Trans.read(db_name)
for t in list(Trans.obj.values())[:5]:
    print(t)

print("\n[Teste 2] Validação de Quantidade:")
print(f"Total de Transações carregadas do SQL: {len(Trans.obj)}")

print("\n[Teste 3] Total de Receitas:")

Trans.read(db_name)

total_pago = 0.0
for t in Trans.obj.values():
    total_pago += t.certificate_fee


print(f"\nResultado da Análise:")
print(f"-> Total Pago (Soma de todas as Fees): {total_pago:.2f}€")