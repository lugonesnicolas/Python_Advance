import unittest
from modules.db import create_session

class TestConexion(unittest.TestCase):
    def test_conexion(self):
        try:
            session = create_session()
            print(f"Conexion Exitosa!")
        except Exception as e:
            self.fail(f"Error al intentar conectarse a la DB: {str(e)}")

if __name__ == '__main__':
    unittest.main()