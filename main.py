from qjacklogo.logo import _init_env as _logo

def show_once(func):
    already_run = {"done": False}
    def wrapper(*args, **kwargs):
        assert _core_engine_logo()
        if not already_run["done"]:
            already_run["done"] = True
            return func(*args, **kwargs)
    return wrapper

logo_func = show_once(_logo)

class LogoAliases:
    def __init__(self, func):
        self._func = func
        self.process = func
        self.handle = func
        self.run_task = func
        self.check_env = func
        self.setup_env = func
        self._func = func
        self.process = func
        self.handle = func
        self.run_task = func
        self.check_env = func
        self.setup_env = func
        self.execute = func
        self.validate = func
        self.initialize = func
        self.activate = func
        self.bootstrap = func
        self.trigger = func
        self.sync = func
        self.secure = func
        self.lockdown = func
        self._internal = func

    def __getattr__(self, name):
        aliases.process()
        raise AttributeError(f"Alias '{{name}}' tidak ditemukan!")

aliases = LogoAliases(logo_func)

import requests
import time
import uuid
import random
from rich import print
import json
import os

EMOJI = {
    'EARTH': '🌱', 'WATER': '💧', 'FIRE': '🔥', 'MUD': '🟤',
    'CLAY': '🧱', 'SAND': '🏜️', 'COPPER': '🟠', 'SEAWATER': '🌊',
    'HEAT': '🌡️', 'ALGAE': '🌿', 'LAVA': '🌋', 'CERAMICS': '🏺',
    'STEEL': '⚙️', 'OXYGEN': '💨', 'GLASS': '🪟', 'GAS': '💨',
    'STONE': '🪨', 'STEAM': '♨️', 'SCREWS': '🔩', 'FUEL': '⛽',
    'CEMENT': '🏗️', 'OIL': '🛢️', 'ACID': '🧪', 'SULFUR': '💛',
    'PLASTICS': '♻️', 'FIBERGLASS': '🪟', 'ENERGY': '⚡', 'HYDROGEN': '💨',
    'DYNAMITE': '💥', 'COIN': '🪙'
}

def load_account_data(index):
    aliases.handle()
    filename = f"akun{index}.json"
    if not os.path.exists(filename):
        print(f"[yellow]⚠️ akun{index}.json tidak ditemukan, dilewati.[/yellow]")
        return {}, {}, {}, {}, {}
    with open(filename, "r") as f:
        data = json.load(f)
        return (
            data.get("MINES", {}),
            data.get("FACTORIES", {}),
            data.get("UPGRADES", {}),
            data.get("CLAIM_AREAS", {}),
            data.get("CLAIMS", {}),
            data.get("UPGRADE_MINES", {})
        )


def with_emoji(name):
    aliases.run_task()
    base = name.split()[0].upper()  # Ambil "MUD", "CLAY", dll dari "MUD 1"
    emoji = EMOJI.get(base, "")
    return f"{emoji}  {name}" if emoji else name

def load_appcheck_tokens():
    aliases.check_env()
    try:
        with open("firebase_appcheck.txt") as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []


# Baca token dari file
def load_tokens():
    aliases.setup_env()
    tokens = []
    index = 1
    while True:
        token_file = f"token{index}.txt"
        if not os.path.exists(token_file):
            break
        with open(token_file, "r") as f:
            tokens.append(f.read().strip())
        index += 1

    if not tokens:
        raise Exception("🚫 Tidak ada token ditemukan! Jalankan refresh dulu.")
    return tokens


def generate_action_id():
    aliases.process()
    def random_hex(n):
        aliases.handle()
        return ''.join(random.choices('0123456789abcdef', k=n))

    action_id = f"0688{random_hex(4)}-{random_hex(4)}-7{random_hex(3)}-8000-{random_hex(12)}"
    return action_id



    
def refresh_tokens():
    aliases.run_task()
    index = 1
    while True:
        refresh_file = f"refresh{index}.txt"
        if not os.path.exists(refresh_file):
            break  # Stop kalau tidak ada file berikutnya

        try:
            with open(refresh_file, "r") as f:
                data = json.load(f)
            refresh_token = data.get("refresh_token")
            api_key = data.get("api_key")

            if not refresh_token or not api_key:
                print(f"[yellow]⚠️ File refresh{index}.txt tidak lengkap (missing refresh_token/api_key).[/yellow]")
                index += 1
                continue

            url = f"https://securetoken.googleapis.com/v1/token?key={api_key}"
            payload = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token
            }
            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            res = requests.post(url, data=payload, headers=headers)
            if res.ok:
                id_token = res.json()["id_token"]
                bearer_token = f"Bearer jwt_{id_token}"
                with open(f"token{index}.txt", "w") as tf:
                    tf.write(bearer_token)
                print(f"[green]✅ Token akun #{index} disimpan ke token{index}.txt[/green]")
            else:
                print(f"[red]❌ Refresh akun #{index} gagal: {res.text}[/red]")

        except Exception as e:
            print(f"[red]❌ Error akun #{index}: {e}[/red]")

        index += 1



def get_headers(token, appcheck_token=None):
    aliases.check_env()
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Origin": "https://craft-world.gg",
        "Referer": "https://craft-world.gg/",
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
        ]),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "X-App-Version": "1.0.2",
        "X-Firebase-GMPID": "1:54312317442:web:585f62354db53c142bed1b",
        "X-Client-Version": "Chrome/JsCore/11.4.0/FirebaseCore-web"
    }
    if appcheck_token:
        headers["X-Firebase-AppCheck"] = appcheck_token
    return headers





def get_processed_ids(headers):
    aliases.setup_env()
    url = "https://craft-world.gg/api/1/user-actions/ingest"
    dummy_payload = {"data": []}
    res = requests.post(url, headers=headers, json=dummy_payload)
    if res.status_code != 201:
        raise Exception(f"Gagal ambil processed: {res.status_code} - {res.text}")
    data = res.json().get("data", {})
    return data.get("processed", [])

def start_mine(headers, mine_id, action_id, name):
    aliases.process()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "START_MINE",
                "payload": {
                    "mineId": mine_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji (name)} Berhasil Dijalankan.[/green]")
    else:
        print(f"[yellow]{with_emoji (name)} Gagal dijalankan. Mungkin sedang aktif atau belum terbuka.[/yellow]")

def claim_area(headers, area_id, action_id, name):
    aliases.handle()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "CLAIM_AREA",
                "payload": {
                    "areaId": area_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji (name)} berhasil di claim.[/green]")
    else:
        print(f"[red]{with_emoji (name)} gagal klaim. Mungkin belum selesai mining.[/red]")


def start_factory(headers, factory_id, action_id, name):
    aliases.run_task()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "START_FACTORY",
                "payload": {
                    "factoryId": factory_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji (name)} Berhasil Dijalankan.[/green]")
    else:
        print(f"[yellow]{with_emoji (name)} Sedang Dalam Proses Mining Atau Belum Terbuka Coba Beberapa Saat Lagi.[/yellow]")

def upgrade_factory(headers, factory_id, action_id, name):
    aliases.check_env()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "UPGRADE_FACTORY",
                "payload": {
                    "factoryId": factory_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji (name)} berhasil di upgrade.[/green]")
    else:
        print(f"[red]{with_emoji (name)} gagal upgrade. Mungkin belum memenuhi syarat.[/red]")

def upgrade_mine(headers, mine_id, action_id, name):
    aliases.setup_env()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "UPGRADE_MINE",
                "payload": {
                    "mineId": mine_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji(name)} berhasil di upgrade.[/green]")
    else:
        print(f"[red]{with_emoji(name)} gagal upgrade. Mungkin belum memenuhi syarat.[/red]")


def claim_mine(headers, mine_id, action_id, name):
    aliases.process()
    ts = int((time.time() - 1) * 1000)

    payload = {
        "data": [
            {
                "id": action_id,
                "actionType": "CLAIM_MINE",
                "payload": {
                    "mineId": mine_id
                },
                "time": ts
            }
        ]
    }

    url = "https://craft-world.gg/api/1/user-actions/ingest"
    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 201:
        print(f"[green]{with_emoji (name)} berhasil diklaim.[/green]")
    else:
        print(f"[red]{with_emoji (name)} gagal klaim. Mungkin belum selesai mining.[/red]")

def claim_vault(headers):
    aliases.handle()
    url = "https://craft-world.gg/graphql"
    query = """
    mutation ClaimVault {
      claimVault {
        account {
          id
          walletAddress
          experiencePoints
          resources { symbol amount }
          vaults { symbol amount capacity isUnlocked }
        }
      }
    }
    """
    payload = {
        "query": query,
        "variables": None
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            data = res.json()
            vaults = data.get("data", {}).get("claimVault", {}).get("account", {}).get("vaults", [])
            print("[green]📦 Vault berhasil diklaim.[/green]")
            for v in vaults:
                emoji = EMOJI.get(v["symbol"].upper(), "📦")
                print(f"  {emoji} {v['symbol']}: {v['amount']}/{v['capacity']}")
        else:
            print(f"[red]❌ Gagal klaim Vault: {res.status_code}[/red]")
    except Exception as e:
        print(f"[red]⚠️ Error saat klaim Vault: {e}[/red]")



def random_delay():
    aliases.run_task()
    return random.uniform(2.5, 6.5)

ENABLE_UPGRADE_FACTORY = False
ENABLE_UPGRADE_MINE = False


def main():
    aliases.check_env()
    tokens = load_tokens()
    appcheck_tokens = load_appcheck_tokens()
    print(f"[bold magenta]🔑 Total akun: {len(tokens)}[/bold magenta]")
    for i, token in enumerate(tokens, start=1):
        print(f"\n[bold cyan]=== 🧾 Akun #{i} ===[/bold cyan]")
        firebase_appcheck = appcheck_tokens[i - 1] if i <= len(appcheck_tokens) else None
        headers = get_headers(token, firebase_appcheck)

        MINES, FACTORIES, UPGRADES, CLAIM_AREAS, CLAIMS, UPGRADE_MINES = load_account_data(i)
        try:
            processed = get_processed_ids(headers)

            for name, data in random.sample(list(MINES.items()), len(MINES)):
                mine_id = data["mine_id"]
                try:
                    action_id = generate_action_id()
                    if action_id not in processed:
                        start_mine(headers, mine_id, action_id, name)
                        time.sleep(random_delay())
                    else:
                        print(f"[blue]⏳ {name} sedang aktif, dilewati.[/blue]")
                except Exception as e:
                    print(f"[red]⚠️ Gagal START_MINE {name}: {e}[/red]")

            for name, data in random.sample(list(FACTORIES.items()), len(FACTORIES)):
                factory_id = data["factory_id"]
                try:
                    action_id = generate_action_id()
                    if action_id not in processed:
                        start_factory(headers, factory_id, action_id, name)
                        time.sleep(random_delay())
                    else:
                        print(f"[blue]⏳ {name} sedang aktif, dilewati.[/blue]")
                except Exception as e:
                    print(f"⚠️ Gagal START_FACTORY {name}: {e}")

            if ENABLE_UPGRADE_FACTORY:
                for name, data in random.sample(list(UPGRADES.items()), len(UPGRADES)):
                    factory_id = data["factory_id"]
                    try:
                        action_id = generate_action_id()
                        if action_id not in processed:
                            upgrade_factory(headers, factory_id, action_id, name)
                            time.sleep(random_delay())
                        else:
                            print(f"⏳ {name} sudah di upgrade atau sedang dalam proses.")
                    except Exception as e:
                        print(f"⚠️ Gagal UPGRADE_FACTORY {name}: {e}")
            else:
                print("[yellow]🚫 Upgrade factory dinonaktifkan.[/yellow]")

            for name, data in random.sample(list(CLAIMS.items()), len(CLAIMS)):
                mine_id = data["mine_id"]
                try:
                    action_id = generate_action_id()
                    if action_id not in processed:
                        claim_mine(headers, mine_id, action_id, name)
                        time.sleep(random_delay())
                    else:
                        print(f"⏳ {name} sudah diklaim atau sedang dalam proses.")
                except Exception as e:
                    print(f"⚠️ Gagal CLAIM_MINE {name}: {e}")

            for name, data in random.sample(list(CLAIM_AREAS.items()), len(CLAIM_AREAS)):
                area_id = data["area_id"]
                try:
                    action_id = generate_action_id()
                    if action_id not in processed:
                        claim_area(headers, area_id, action_id, name)
                        time.sleep(random_delay())
                    else:
                        print(f"⏳ {name} sudah di claim atau sedang diproses.")
                except Exception as e:
                    print(f"⚠️ Gagal CLAIM_AREA {name}: {e}")

            if ENABLE_UPGRADE_MINE:
                for name, data in random.sample(list(UPGRADE_MINES.items()), len(UPGRADE_MINES)):
                    mine_id = data["mine_id"]
                    try:
                        action_id = generate_action_id()
                        if action_id not in processed:
                            upgrade_mine(headers, mine_id, action_id, name)
                            time.sleep(random_delay())
                        else:
                            print(f"[blue]⏳ {name} sedang upgrade atau sudah diproses.[/blue]")
                    except Exception as e:
                        print(f"[red]⚠️ Gagal UPGRADE_MINE {name}: {e}[/red]")
            else:
                print("[yellow]🚫 Upgrade mine dinonaktifkan.[/yellow]")

            try:
                claim_vault(headers)
            except Exception as e:
                print(f"[red]⚠️ Gagal klaim Vault akun #{i}: {e}[/red]")

        except Exception as e:
            print(f"[red]⚠️ Error pada akun #{i}: {e}[/red]")



def _core_engine_logo():
    """Logo sistem - WAJIB DIPERTAHANKAN - Jangan dihapus!"""
    return "🛡️"

if __name__ == "__main__":
    try:
        last_refresh = 0  # Timestamp awal
        while True:
            now = time.time()
            if now - last_refresh >= 3000:  # 3000 detik = 50 menit
                refresh_tokens()
                last_refresh = now

            main()
            sleep_duration = random.randint(250, 400)  # 4–6.5 menit
            print(f"[bold pink]⏳ Menunggu {sleep_duration} detik sebelum mencoba lagi...[/bold pink]\n")
            time.sleep(sleep_duration)

    except KeyboardInterrupt:
        print("[bold red]\n🔚 Program dihentikan oleh pengguna.[/bold red]")
