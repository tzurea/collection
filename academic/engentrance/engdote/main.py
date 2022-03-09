import argparse
from engdote.engdote import engdote, create_db_tables


argument_parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

argument_parser.add_argument(
    "--token", type=str, required=False, help="Token to use to query "
)
argument_parser.add_argument(
    "--type",
    type=str,
    required=False,
    help="""Type of test to fetch 
            pea : IOE BE Entrance Saturday Mock Test
            csit : TU BCSIT Entrance Saturday Mock Test
            daily : IOE BE Entrance Daily Capsule
            be : IOE BE Entrance Model Mock Test
            qbank : IOE BE Entrance Question Bank """,
)
argument_parser.add_argument("--db", action="store_true", help="Initialize database")

arguments = argument_parser.parse_args()
test_type = arguments.type

if arguments.db:
    create_db_tables()

if __name__ == "__main__":
    engdote(test_type=test_type)
