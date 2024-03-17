import 'package:dartdoc/dartdoc.dart';
import 'package:path/path.dart' as path;

Future<void> generateAPIReference(String inputPath, String outputPath) async {
  // Load the input file.
  final inputFile = File(inputPath);
  final inputContents = await inputFile.readAsString();

  // Parse the input file into a Document.
  final document = Document.fromString(inputContents);

  // Generate the API reference documentation.
  final apiReference = document.generateAPIReference();

  // Save the API reference documentation to the output file.
  final outputFile = File(outputPath);
  await outputFile.writeAsString(apiReference);
}
