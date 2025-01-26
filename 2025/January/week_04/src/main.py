from config.settings import Settings
from services.service_manager import ServiceManager

def main():
    settings = Settings()
    service_manager = ServiceManager(settings)
    service_manager.initialize()

if __name__ == "__main__":
    main()