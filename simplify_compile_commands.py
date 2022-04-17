import json
import pathlib
import re
from json import load
import logging

logging.basicConfig(
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

root_map = {
    r'E:\\': r'/dev/e/'
}


def get_file_mapper_func(file_map):
    file_map_func = []
    for regex, sub_string in file_map.items():
        logger.info('map %s to %s', regex, sub_string)
        file_map_func.append((re.compile(regex).sub, sub_string))

    def mapper(file_path):
        mapped_file_path = file_path
        for map_func, sub in file_map_func:
            mapped_file_path = map_func(sub, mapped_file_path)
        logger.debug('map %s to %s', file_path, mapped_file_path)

    return mapper


def get_compiler_commands() -> list:
    logger.info('load the number of cmd is %d')
    return []


def get_defects() -> list:
    logger.info('load the number of defects is %d')
    return []


def to_defects_file_set(defects: list) -> set:
    logger.info('the number of defects file set is %d')
    return set()


def to_compiler_commands_table(compile_cmd: list) -> dict:
    for cmd in compile_cmd:
        logger.debug('current compiler file is %s')
        logger.debug('output compiler file is %s')
    return dict()


def filter_compiler_commands_by_files(compiler_cmd_table: dict, defects_file_set: set) -> list:
    sim_compiler_commands = []
    for file in defects_file_set:
        if file in compiler_cmd_table.keys():
            compiler_cmd  = compiler_cmd_table[file]
            logger.info('find %d for %s', len(compiler_cmd), file)
            sim_compiler_commands.extend(compiler_cmd_table[file])
        else:
            logger.warning('no found %s', file)
    return sim_compiler_commands


def main():
    compiler_commands = get_compiler_commands()
    defects = get_defects()

    defects_file = to_defects_file_set(defects)

    compiler_cmd_table = to_compiler_commands_table(compiler_commands)

    sim_compiler_commands = filter_compiler_commands_by_files(compiler_cmd_table, defects_file)

    sim_compiler_commands = [{'file': '123'}]
    with open('compile_commands.simplify.json', 'w', encoding='utf-8') as f:
        json.dump(sim_compiler_commands, f, sort_keys=True, indent=2)


if __name__ == "__main__":
    root_mapper_func = get_file_mapper_func(root_map)
    for path in pathlib.Path('./').glob('**/*.py'):
        root_mapper_func(str(path.absolute()))

