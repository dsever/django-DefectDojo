import json
import logging

from django.core.management.base import BaseCommand
from dojo.models import Test_Type
from dojo.tools import factory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Dumps json file of supported scanners or directly re-sync it to the DB
    this is quick and dirty, TODO: refactor
    """

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file_path", required=False, help="Dump tools into the file")
        parser.add_argument("-r", "--resync", action="store_true", help="Add new scanners to database")
        parser.add_argument("-d", "--dump", action="store_true", help="Print to standard output")
        parser.add_argument("-i", "--inconsistency", action="store_true", help='Look for inconsistency')

    def handle(self, *args, **options):
        counter = 100
        model = "dojo.Tool_Type"
        dump = []
        # This stupid workarround sets factory to start with pk 100
        try:
            Test_Type.objects.filter(name="Reservation").delete()
        except:
            pass

        for parser in factory.PARSERS:
            for scan_type in factory.PARSERS[parser].get_scan_types():
                dump.append(
                    {
                        "model": model,
                        "pk": counter,
                        "fields": {
                            "name": scan_type,
                            "description": factory.PARSERS[parser].get_description_for_scan_types(scan_type),
                        },
                    }
                )
                if options["resync"]:
                    try:
                        logger.debug("Sync {0}".format(scan_type))
                        test_type, created = Test_Type.objects.get_or_create(
                            name=scan_type
                        )
                        if created:
                            test_type.description = factory.PARSERS[parser].get_description_for_scan_types(scan_type),
                            logger.info("Creating {0}".format(test_type.name))

                    except Exception as e:
                        logger.exception(e)

            counter += 1
        if options["file_path"]:
            logger.info("writing to {0}".format(options["file_path"]))
            file = open(options["file_path"], "a")
            file.write(json.dumps(dump, indent=2))
            file.close()
        if options["dump"]:
            print(json.dumps(dump, indent=2))
        if options["inconsistency"]:

            tools = Test_Type.objects.all()
            print("Missing in DB")
            for parser in factory.PARSERS:
                if tools.filter(name=parser).count() == 0:
                    print("\t {}".format(parser))
            print("Missing in factory")
            for tool in tools:
                if tool.name not in factory.PARSERS:
                    print("\t {}".format(tool.name))




