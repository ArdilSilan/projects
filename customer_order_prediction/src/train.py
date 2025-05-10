
def train_model(model, X_train, y_train, X_test, y_test, epochs=50):
    model.fit(X_train, y_train, epochs=epochs, validation_data=(X_test, y_test),verbose=1)

    model.save('outputs/model.h5')