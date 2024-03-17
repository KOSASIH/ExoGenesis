using System;
using System.IO;
using MediaFoundation;

public static void ConvertAudioToMP3(string inputFilePath, string outputFilePath)
{
    // Create a Media Foundation source reader
    using (var sourceReader = new MediaFoundationReader(inputFilePath))
    {
        // Create a Media Foundation sink writer
        using (var sinkWriter = new MFSinkWriter(outputFilePath, sourceReader.WaveFormat))
        {
            // Set the input format for the sink writer
            sinkWriter.SetInputFormat(0, sourceReader.WaveFormat);

            // Read samples from the source reader
            byte[] buffer = new byte[sourceReader.WaveFormat.AverageBytesPerSecond];
            int bytesRead;
            while ((bytesRead = sourceReader.Read(buffer, 0, buffer.Length)) > 0)
            {
                // Write samples to the sink writer
                sinkWriter.WriteSample(0, buffer, bytesRead);
            }
        }
    }
}
