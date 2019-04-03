import argparse
import anago

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test a model')
    parser.add_argument('--weights_file', default='weights.h5', help='weights file')
    parser.add_argument('--params_file', default='params.json', help='parameter file')
    parser.add_argument('--preprocessor_file', default='preprocessor.json', help='preprocessor file')
    args = parser.parse_args()

    model = anago.Sequence.load(args.weights_file, args.params_file, args.preprocessor_file)
    # input = "水戸藩 の 二代 藩主 、 徳川光圀 など が まつら れ て いる 水戸市 の 常磐神社 で 、 ことし １ 年間 に たまっ た ほこり を 落とし 、 新年 を 迎える ため の すす払い が 行わ れ まし た "
    while True:
        print(model.analyze(input()))
