package com.emptyredoubt.vaadinTest;

import org.springframework.data.jpa.repository.JpaRepository;

import javax.transaction.Transactional;

/**
 * Created by theuser on 6/16/2017.
 */
public interface TodoRepository extends JpaRepository<Todo, Long>{
    @Transactional
    void deleteByDone(boolean done);
}
