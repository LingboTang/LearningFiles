/**
 * Created by lingbo on 21/02/17.
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.filters.Filter;
import weka.filters.supervised.attribute.AttributeSelection;
import weka.classifiers.functions.LinearRegression;
import weka.core.FastVector;
import weka.core.Instances;


public class IscoreRegression {


    public static BufferedReader readDataFile(String filename) {
        BufferedReader inputReader = null;

        try {
            inputReader = new BufferedReader(new FileReader(filename));
        } catch (FileNotFoundException ex) {
            System.err.println("File not found: " + filename);
        }

        return inputReader;
    }

    public static Evaluation classify(Classifier model, Instances trainingSet,
                                      Instances testingSet) throws Exception {
        Evaluation evaluation = new Evaluation(trainingSet);
        model.buildClassifier(trainingSet);
        evaluation.evaluateModel(model, testingSet);
        return evaluation;
    }

    public static Instances[][] crossValidationSplit(Instances data, int numberOfFolds) {
        Instances[][] split = new Instances[2][numberOfFolds];
        for (int i = 0; i < numberOfFolds; i++) {
            split[0][i] = data.trainCV(numberOfFolds, i);
            split[1][i] = data.testCV(numberOfFolds, i);
        }
        return split;
    }

    /*public static double calculateIscore(Instances data, int numOfCells, int numOfindividualsInOneCell) throws Exception {
        double yMean = data.meanOrMode(data.classIndex());
        double tss = 0.0;

        double meanSEofCell = 0.0;

        for (int j = 0; j<numOfCells; j++) {
            meanSEofCell += (data.instance(j).value(data.classIndex())-yMean) * (data.instance(j).value(data.classIndex())-yMean) * numOfindividualsInOneCell;
        }

        for (int i = 0; i < data.numInstances(); i++) {
            tss += (data.instance(i).value(data.classIndex()) - yMean) * (data.instance(i).value(data.classIndex()) - yMean);
        }

        return meanSEofCell/tss;
    }*/

    public static void main(String[] args) throws Exception {
        /*
         * Parse data from arff files
         */
        BufferedReader datafile = readDataFile("/home/lingbo/Desktop/LearningFiles/Data/exactAttributes.arff");
        Instances data = new Instances(datafile);
        data.setClassIndex(data.numAttributes() - 1);

        /*
         * Filtering Data, currently I used the ChiSquareSubsetEvaluation
         * and GreedyStepwise to run a stepwise regression on the data.
         * This will help us reduce the dimention of original data.
         */
        AttributeSelection mySelection = new AttributeSelection();
        mySelection.setOptions(weka.core.Utils.splitOptions("-E \"weka.attributeSelection.CfsSubsetEval -P 1 -E 1\" -S \"weka.attributeSelection.GreedyStepwise -T -1.7976931348623157E308\" "));
        mySelection.setInputFormat(data);
        Instances filteredData = Filter.useFilter(data, mySelection);

        /*
         * Build our linear regression model with options
         * Stepwise regression, greedy critiria and threshold settings
         * Print out the final model we have
         */

        LinearRegression silicoRegression = new LinearRegression();
        silicoRegression.setOptions(weka.core.Utils.splitOptions("-S 2 -R 1.0E-8 -additional-stats -num-decimal-places 4"));
        silicoRegression.buildClassifier(filteredData);
        System.out.println(silicoRegression);

        /*
         * Use cross validate to get more accurate linear regression model
         */

        Instances[][] split = crossValidationSplit(filteredData, 10);

        Instances[] trainingSplits = split[0];
        Instances[] testingSplits = split[1];


        FastVector predictions = new FastVector();

        for (int i = 0; i < trainingSplits.length; i++) {
            Evaluation validation = classify(silicoRegression, trainingSplits[i], testingSplits[i]);
            predictions.appendElements(validation.predictions());
        }


        for (int i =0; i< predictions.size(); i++) {
            System.out.println(predictions.get(i));
        }
    }
}