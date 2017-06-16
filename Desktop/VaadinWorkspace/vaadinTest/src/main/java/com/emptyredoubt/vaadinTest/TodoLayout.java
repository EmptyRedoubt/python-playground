package com.emptyredoubt.vaadinTest;
import com.vaadin.spring.annotation.SpringComponent;
import com.vaadin.spring.annotation.UIScope;
import com.vaadin.ui.VerticalLayout;
import org.springframework.beans.factory.annotation.Autowired;

import javax.annotation.PostConstruct;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by theuser on 6/16/2017.
 */
@UIScope
@SpringComponent
class TodoLayout extends VerticalLayout implements TodoChangeListener{
    @Autowired
    TodoRepository repo;
    private List<Todo> todos;


    @PostConstruct
    void init(){
        setWidth("80%");
        update();
    }

    private void update() {
        setTodos(repo.findAll());
    }

    private void setTodos(List<Todo> todos) {
        this.todos = todos;
        removeAllComponents();
        todos.forEach(todo -> addComponent(new TodoItemLayout(todo, this)));
    }

    void addTodo(Todo todo) {
        repo.save(todo);
        update();
    }


    public void deleteCompleted() {
        repo.deleteInBatch(
                todos.stream().filter(Todo::isDone).collect(Collectors.toList())
        );
        repo.deleteByDone(true);
        update();
    }

    @Override
    public void TodoChanged(Todo todo) {
        addTodo(todo);

    }
}
