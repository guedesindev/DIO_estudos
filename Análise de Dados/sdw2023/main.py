from extract import extract_data
from transform import transform_data
from load import load_data

# from load import load_data
import time


def run_pipline():
    print("\n" + "=" * 50)
    print("      🏦 SANTANDER ETL - INTELLIGENT MESSAGING")
    print("=" * 50 + "\n")

    print("🔎 [1/3] EXTRAÇÃO: lendo arquivos CSV de usuarios e IDs...")
    try:
        df_usuarios, df_ids = extract_data()
        print(f"✅ Scucesso: {len(df_usuarios)} usuarios carregados.\n")
        print("-" * 30)
    except Exception as e:
        print(f"❌ Erro na extração: {e}")

    time.sleep(1)

    print("⚙️ [2/3] TRANSFORMAÇÃO: Gerando mensagens e processando lógica...")
    try:
        df_final = transform_data(df_usuarios, df_ids)
        print(f"\n✅ {len(df_final)} mensagens geradas com sucesso.")
        print("-" * 30)
    except Exception as e:
        print(f"❌ Erro na transformação: {e}")
        return

    time.sleep(1)

    print(f"💾 [3/3] CARREGAMENTO: A gravar no news.csv...")
    try:
        load_data(df_final)
        print("✅ Sucesso: Dados integrados com êxito!\n")
    except Exception as e:
        print(f"❌ Erro no Carregametno: {e}")
        return

    print("\n" + "=" * 50)
    print("🎯 Pipeline concluído com sucesso!")
    print("\n-" + "=" * 50)


if __name__ == "__main__":
    run_pipline()
